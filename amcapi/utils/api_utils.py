import re

from mongoengine import errors as mngoengerrs

from amcweb.models import WhatsappSubscriber


def subscribe_whatsapp(number):
    valid_number = re.match(r'^\+?[0-9]{10,18}$', number)
    if valid_number:
        new_subscriber = WhatsappSubscriber(phone=valid_number.group(0))
        try:
            new_subscriber.save()
            return True
        except mngoengerrs.ValidationError:
            print('Unable to add to whatsapp subscribers list')
            return False
    else:
        return False
