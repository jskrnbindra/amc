from datetime import date

from django import forms

from .config import APPOINTMENT_TYPES


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

    def send_email(self):
        print('send email')
        pass
