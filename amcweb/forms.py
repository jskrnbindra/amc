from datetime import date

from django import forms

from .config import APPOINTMENT_TYPES


class AppointmentForm(forms.Form):
    name = forms.CharField(max_length=50)
    contact = forms.CharField(max_length=10)
    email = forms.EmailField(required=False)
    gender = forms.ChoiceField(choices=[(-1, '--'), (0, 'Male'), (1, 'Female'), (2, 'Rather not mention')])
    birth_year = forms.ChoiceField(choices=[(-1, '--')] + [x for x in list(map(lambda x: (x,x) ,reversed(range(1901, date.today().year + 1))))])
    visiting_on = forms.DateTimeField(input_formats=['%m/%d/%Y %H:%M'])
    purpose = forms.ChoiceField(choices=[(-1, '--')] + [(i + 1, x) for i, x in enumerate(APPOINTMENT_TYPES)])
    comment = forms.CharField(required=False, max_length=500, widget=forms.Textarea)

    def send_email(self):
        print('send email')
        pass
