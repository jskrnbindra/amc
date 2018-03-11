from amcweb.utils.send_mail import SendMail

from amcweb.config import EMAIL_TEMPLATES


def mail(email_template, context, inform_admin=True):

    print('sending mail to client')
    SendMail(email_context(email_template, context)).start()

    if inform_admin:
        print('sending mail to admin')
        SendMail(email_context_admin(email_template, context)).start()


def email_context(email_template, context):
    template = EMAIL_TEMPLATES[email_template]
    return {
        'subject': template['subject'],
        'body': template['body'] % context['name'],
        'from': template['from'],
        'to': [context['email']]
    }


def email_context_admin(email_template, context):
    template = EMAIL_TEMPLATES[email_template + '_admin']
    return {
        'subject': template['subject'] % context['name'],
        'body': template['body'] % context['name'],
        'from': template['from'],
        'to': template['to']
    }
