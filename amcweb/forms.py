from datetime import date

from django import forms

class AppointmentForm(forms.Form):
    name = forms.CharField(max_length=50,required=False)
    contact = forms.CharField(max_length=10,required=False)
    email = forms.EmailField(required=False)
    gender = forms.ChoiceField(required=False,choices=[(-1, '--'), (0, 'Male'), (1, 'Female'), (2, 'Rather not mention')])
    birth_year = forms.ChoiceField(required=False,choices=[(-1, '--')] + [x for x in list(map(lambda x: (x,x) ,reversed(range(1901, date.today().year + 1))))])
    visiting_on = forms.DateTimeField(input_formats=['%m/%d/%Y %H:%M'])

    def send_email(self):
        print('send email')
        pass
