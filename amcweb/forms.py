from datetime import datetime, date

from django import forms

from  amcweb.utils.mongo_utils import next_count
from .config import APPOINTMENT_TYPES
from .models import Patient, Appointment


def required_msg(required_suffix):
    return f'You forgot to enter {required_suffix}.🤷‍'

def invalid_msg(invalid_suffix):
    return f'That does not looks like a valid {invalid_suffix}.🧐'

def get_errors(invalid_suffix, required_suffix):
    return {
        'invalid': invalid_msg(invalid_suffix),
        'required': required_msg(required_suffix)
    }


class AppointmentForm(forms.Form):
    name = forms.RegexField(strip=True, regex='^[a-zA-Z. ]+$', max_length=50, error_messages=get_errors('name', 'your name'))
    contact = forms.RegexField(strip=True, regex='^[0-9]{10}$', max_length=10, error_messages=get_errors('phone number', 'your phone number'))
    email = forms.EmailField(required=False, error_messages=get_errors('email', 'your email'))
    gender = forms.ChoiceField(choices=[(-1, '--'), ('Male', 'Male'), ('Female', 'Female'), ('Rather not mention', 'Rather not mention')], error_messages=get_errors('gender', 'your gender'))
    birth_year = forms.ChoiceField(choices=[(-1, '--')] + [x for x in list(map(lambda x: (x, x), reversed(range(1901, date.today().year + 1))))], error_messages=get_errors('birth year', 'your birth year'))
    visiting_on = forms.DateTimeField(input_formats=['%m/%d/%Y %H:%M'], error_messages=get_errors('visiting date', 'a visiting date'))
    purpose = forms.ChoiceField(choices=[(-1, '--')] + [(x, x) for i, x in enumerate(APPOINTMENT_TYPES)], error_messages=get_errors('appointment type', 'an appointment type'))
    comment = forms.RegexField(strip=True, regex='^[a-zA-Z0-9. ]+$', required=False, max_length=500, widget=forms.Textarea, error_messages=get_errors('comment', 'comment'))
    patient_id = forms.IntegerField(required=False, min_value=1, error_messages=get_errors('patient number', 'your patient number'))

    def clean_gender(self):
        if self.cleaned_data['gender'] == '-1':
            raise forms.ValidationError('You forgot to select a gender.🤷‍')
        else:
            return self.cleaned_data['gender']

    def clean_birth_year(self):
        if self.cleaned_data['birth_year'] == '-1':
            raise forms.ValidationError('You forgot to select a birth year.🤷‍')
        else:
            return self.cleaned_data['birth_year']

    def clean_purpose(self):
        if self.cleaned_data['purpose'] == '-1':
            raise forms.ValidationError('You forgot to select an appointment type.🤷‍')
        else:
            return self.cleaned_data['purpose']

    def clean_patient_id(self):
        if self.cleaned_data['patient_id']:
            patient_id = int(self.cleaned_data['patient_id'])
            existing = Patient.objects(uid=patient_id)
            self.cleaned_data['patient'] = None if not existing else existing[0]
        else:
            self.cleaned_data['patient'] = None

        return self.cleaned_data['patient_id']

    def send_email(self):
        print('mail sent')

    def update_patient(self, appointment_form):
        patient = self.cleaned_data['patient']
        patient.contact += [appointment_form['contact']] if not appointment_form['contact'] in patient.contact else []
        patient.email += [appointment_form['email']] if not appointment_form['email'] in patient.email else []

        return patient

    def has_duplicate(self, patient):
        possible_duplicates = Patient.objects(contact=patient.contact[0])
        duplicates = []

        for possible_duplicate in possible_duplicates:
            names_match = possible_duplicate['first_name'].lower().strip() == patient['first_name'].lower().strip()
            genders_match = possible_duplicate['gender'].lower() == patient['gender'].lower()
            birth_years_match = True if possible_duplicate['dob'] is None else possible_duplicate['dob'].year() == int(patient['birth_year'])

            if names_match and genders_match and birth_years_match:
                duplicates.append(possible_duplicate)

        if len(duplicates) > 1:
            print('Multiple duplicates found for a record. Looks like an error. This is an error.')
        elif len(duplicates) == 0:
            return None
        elif len(duplicates) == 1:
            return duplicates[0]
        else:
            print('Unexpected code path followed. This is an error.')

    def new_patient(self, appointment_form):
        appointment_form['name'] += ' ' if ' ' not in appointment_form['name'] else ''
        new_pat = Patient(
            uid=next_count('Patient'),
            first_name=appointment_form['name'][:appointment_form['name'].index(' ')],
            last_name=appointment_form['name'][appointment_form['name'].rindex(' ') + 1:],
            gender=appointment_form['gender'].lower(),
            contact=[appointment_form['contact']] if 'contact' in appointment_form else [],
            email=[appointment_form['email']] if appointment_form['email'] != '' else [],
            problem=appointment_form['purpose'],
            comments=appointment_form['comment'],
            prescriptions=[],
            appointments=[]
        )

        any_duplicate = self.has_duplicate(new_pat)

        return any_duplicate if any_duplicate else new_pat

    def create_appointment(self, appointment_form):
        print(appointment_form)
        if not appointment_form['patient']:  # new patient
            patient = self.new_patient(appointment_form)
        else:  # existing patient
            patient = self.update_patient(appointment_form)

        new_appointment = Appointment(
            uid=next_count('Appointment'),
            datetime=appointment_form['visiting_on'],
            new_patient=False if appointment_form['patient'] else True,
            applied_on=datetime.now(),
            purpose=appointment_form['purpose'],
            requested_through='website',
            patient_id=patient['uid'],
        )

        patient['appointments'].append(new_appointment)
        patient.save()


# wrong patient id entered case......kinda handeled with name lookup
# duplicate patient created on new_patient
# dad bookin an appointment by filling his details but appointment is for kid


class SubscribeEmail(forms.Form):
    email = forms.EmailField(required=False, error_messages=get_errors('email', 'your email'))

    def done_here(self):
        print('done ho gya')
