
from rapidsms.apps.base import AppBase
import re

from .models import MobilePayment,MClient

class App(AppBase):
    def handle (self, message):
        reg=re.compile(r'(\d+(,\d+)?)')
        text=message.text
        country_code="256"
        try:
            amount,sender,balance=map(lambda x:x[0].replace(",",""),reg.findall(text))
            if sender.startswith('0'):
                number = '%s%s' % (country_code, sender[1:])
            elif number.startswith('+'):
                number = '%s' % sender[1:]
            elif number[:len(country_code)] != country_code:
                number = '%s%s' % (country_code, sender)

            payment=MobilePayment.objects.create(sender=number,amount=amount)
            try:
                client=MClient.objects.get(external_id=sender)
                payment.client=client
                payment.save()
            except MClient.DoesNotExist:
                pass
        except ValueError:
            pass


        return True