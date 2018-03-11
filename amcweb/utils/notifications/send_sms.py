import threading

from urllib import request, parse

from amcweb.config import SMS_API_KEY, SMS_API_URL, SMS_TEST_MODE


class SendSMS(threading.Thread):
    """
    Sends an SMS in a new thread.
    """

    def __init__(self, sms_msg):
        threading.Thread.__init__(self)
        self.sms_msg = sms_msg

    def run(self):
        print(self.sms())

    def sms(self):
        """
        Sends an SMS via HTTP.
        :return: HTTPResponse
        """
        try:
            req = request.Request(SMS_API_URL)
            params = parse.urlencode({
                'apikey': SMS_API_KEY,
                'sender': self.sms_msg['sender'],
                'numbers': self.sms_msg['to'],
                'message': self.sms_msg['body'],
                'test': 'true' if SMS_TEST_MODE else 'false'
            })
            response = request.urlopen(req, params.encode('utf-8'))
            return response.read()
        except Exception as e:
            print(f'Error:  Could not send SMS.{e}')
            return None
