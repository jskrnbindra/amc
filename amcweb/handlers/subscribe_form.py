from amcweb.utils.notifications.smser import send_sms

from mongoengine import errors as mngoengerrs
from pymongo import errors

from amcweb.models import Subscriber, WhatsappSubscriber  # Don't remove these imports, they're used
from amcweb.utils.notifications.mailer import mail


def new_subscriber_handler(request):
    phone = request.POST['phone'] if len(request.POST['phone']) > 0 else None
    subscriber = Subscriber(request.POST['email'], request.POST['name'], phone)
    try:
        new_sub = subscriber.save()
    except errors.AutoReconnect:
        context = {
            'err': 'DB_CONN_ERR',
            'msg': "Oops! There was an error. Please try after some time."
        }
        return context
    except mngoengerrs.ValidationError as err:
        print(err)
        context = {
            'err': 'BAD_INPUT',
            'msg': "There were errors in the info you entered. Enter valid info.",
            'form': request.POST
        }
        return context

    context = {'msg': "You've been subscribed to the newsletter. 🙂"}
    mail('new_subscriber', {'name': new_sub.name, 'email': new_sub.email})
    send_sms('new_subscriber', {'name': new_sub.name, 'numbers': phone})

    return context


def new_whatsapp_subscriber_handler(request):
    name = request.POST['name'] if len(request.POST['name']) > 0 else None
    subscriber = WhatsappSubscriber(name, request.POST['phone'])
    try:
        new_sub = subscriber.save()
    except errors.AutoReconnect:
        context = {
            'err': 'DB_CONN_ERR',
            'msg': "Oops! There was an error. Please try after some time."
        }
        return context
    except mngoengerrs.ValidationError as err:
        print(err)
        context = {
            'err': 'BAD_INPUT',
            'msg': "There were errors in the info you entered. Enter valid info.",
            'form': request.POST
        }
        return context

    context = {'msg': "You've been subscribed to whatsapp updates. 🙂"}
    mail('new_whatsapp_subscriber', {'name': new_sub.name, 'numbers': new_sub.phone})
    send_sms('new_whatsapp_subscriber', {'name': new_sub.name, 'numbers': new_sub.phone})

    return context
