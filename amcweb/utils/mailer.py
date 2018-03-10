from django.core.mail import send_mail

from amcweb.config import EMAIL_TEMPLATES


def mail(email_template, context):
    template = EMAIL_TEMPLATES[email_template]
    send_mail(
        template['subject'],
        template['body'] % context['name'],
        template['from'],
        [context['email']],
        fail_silently=False
        )

    template = EMAIL_TEMPLATES[email_template + '_admin']
    send_mail(
        template['subject'] % context['name'],
        template['body'] % context['name'],
        template['from'],
        template['to'],
        fail_silently=False
    )
