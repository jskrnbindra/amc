from django import forms

class AppointmentForm(forms.Form):
    name = forms.CharField()
    # message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        print('send email')
        pass

    def clean_name(self):
        print('clean the name here bro')
        return self.cleaned_data['name']