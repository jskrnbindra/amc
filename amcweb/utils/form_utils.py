
def required_msg(required_suffix):
    return f'You forgot to enter {required_suffix}.🤷‍'


def invalid_msg(invalid_suffix):
    return f'That does not looks like a valid {invalid_suffix}.🤔'


def get_errors(invalid_suffix, required_suffix):
    return {
        'invalid': invalid_msg(invalid_suffix),
        'required': required_msg(required_suffix)
    }
