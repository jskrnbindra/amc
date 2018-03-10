import urllib.request
import urllib.parse
from amcweb.config import SMS_API_KEY, SMS_API_URL, SMS_TEMPLATES


def send_sms(sms_template, context):
    template = SMS_TEMPLATES[sms_template]
    data = urllib.parse.urlencode({'apikey': SMS_API_KEY,
                                   'numbers': context['numbers'],
                                   'message': template['body'] % context['name'],
                                   'sender': template['from']
                                   })
    data = data.encode('utf-8')
    request = urllib.request.Request(SMS_API_URL)
    f = urllib.request.urlopen(request, data)
    resp = f.read()
    read_sms_resp(resp)

    template = SMS_TEMPLATES[sms_template + '_admin']
    data = urllib.parse.urlencode({'apikey': SMS_API_KEY,
                                   'numbers': context['numbers'],
                                   'message': template['body'] % context['name'],
                                   'sender': template['from']
                                   })
    data = data.encode('utf-8')
    f = urllib.request.urlopen(request, data)
    print('admin sms response')
    print(f.read())

    return resp


def read_sms_resp(resp):
    print(resp)
