from django.test import TestCase

# Create your tests here.
from .models import shipd, orderss

# django 2.x
from django.urls import reverse

import datetime

# Create your tests here.
class hello(TestCase):
    def test_page_is_for_orderss_created_successfully(self):
        a1d=datetime.date(2021,6,3)
        a1=orderss(sen_name = 'Ahamed' , sen_add = '24/08 Chennai' , sen_ph = '7896541232' ,rec_name = 'Irshad' , rec_add = '24/08 Chennai' , rec_ph = '7896541232' , t_g = 'Eatables', orgin = 'Chennai', dest = 'Osaka', pri = 'Urgent', nodays=2, weight=10,  rej=1, cost=20, shipid=1,dd='04',dm='Month',dy='2021',ddd=a1d)
        a1.save()




        


