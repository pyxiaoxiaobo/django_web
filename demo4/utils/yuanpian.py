import requests


class YunPian(object):
    def __int__(self, api_key):
        self.api_key = api_key
        self.single_send_url = 'HTTPS://sms.yunpian.com/v2/sms/single_send.json'

    def send_sms(self, code, mobile):
        parms = {
            'apikey': self.api_key,
            'mobile': mobile,
            # 跟云片网后天模板内容保持一致
            'text': "您的验证码是{code}。如非本人操作请忽略".format(code=code),
        }
        r = requests.post(self.single_send_url, data=parms)
        print(r)