from functools import reduce

from amcweb.config import SMS_TEMPLATES
from amcweb.utils.send_sms import SendSMS


def send_sms(sms_template, context, inform_admin=True):
    if context['numbers']:
        SendSMS(sms_context(sms_template, context)).start()

    if inform_admin:
        SendSMS(sms_context_admin(sms_template, context)).start()


def sms_context(sms_template, context):
    template = SMS_TEMPLATES[sms_template]
    return {
        'body': template['body'] % context['name'],
        'sender': template['from'],
        'to': context['numbers']
    }


def sms_context_admin(sms_template, context):
    template = SMS_TEMPLATES[sms_template + '_admin']
    return {
        'body': template['body'] % context['name'],
        'sender': template['from'],
        'to': reduce(lambda x, y: f'{x},{y}', template['to'], '').strip(',')
    }
