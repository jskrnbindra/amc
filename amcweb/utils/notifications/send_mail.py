import threading

from smtplib import SMTPException

from django.core.mail import send_mail


class SendMail(threading.Thread):
    """
    Sends a mail in a new thread.
    """

    def __init__(self, email):
        threading.Thread.__init__(self)
        self.email = email

    def run(self):
        self.mail()

    def mail(self):
        try:
            send_mail(
                self.email['subject'],
                self.email['body'],
                self.email['from'],
                self.email['to'],
                fail_silently=False
            )
            print(f"Mail sent to:{self.email['to']}")
        except SMTPException:
            print(f'Error: Mail could not be sent.')
