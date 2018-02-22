from datetime import datetime, date

from django import forms

from  amcweb.utils.mongo_utils import next_count


def required_msg(required_suffix):
    return f'You forgot to enter {required_suffix}.🤷‍'

def invalid_msg(invalid_suffix):
    return f'That does not looks like a valid {invalid_suffix}.🧐'

def get_errors(invalid_suffix, required_suffix):
    return {
        'invalid': invalid_msg(invalid_suffix),
        'required': required_msg(required_suffix)
    }


class SubscribeEmail(forms.Form):
    email = forms.EmailField(required=False, error_messages=get_errors('email', 'your email'))

    def done_here(self):
        print('done ho gya')
