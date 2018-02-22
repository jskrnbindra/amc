from .forms import SubscribeEmail


def email_subscribe(request):
    return {
        'email_subscribe': SubscribeEmail()
    }
