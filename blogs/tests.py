from django.test import TestCase

# Create your tests here.
from .models import shipd, orderss

# django 2.x
from django.urls import reverse

import datetime

# Create your tests here.
class hello(TestCase):
    def test_page_is_for_shipd_created_successfully(self):
        a1d=datetime.date(2021,6,3)
        a1=shipd(shipid=1,shname='MCP-101',shorig='Miami',shdest='Cape Town',shdate=a1d,con_e=0,con_f=0,con_s=0)
        a1.save()
        a11d=datetime.date(2021,6,3)
        a11=shipd(shipid=1,shname='MCP-101',shorig='Miami',shdest='Cape Town',shdate=a11d,con_e=0,con_f=0,con_s=0)
        a11.save()

    def test_page_is_for_orderss_created_successfully(self):
        a1d=datetime.date(2021,6,3)
        a1=orderss(sen_name = 'Ahamed' , sen_add = '24/08 Chennai' , sen_ph = '7896541232' ,rec_name = 'Irshad' , rec_add = '24/08 Chennai' , rec_ph = '7896541232' , t_g = 'Eatables', orgin = 'Chennai', dest = 'Osaka', pri = 'Urgent', nodays=2, weight=10,  rej=1, cost=20, shipid=1,dd='04',dm='Month',dy='2021',ddd=a1d)
        a1.save()

class urlss(TestCase):
    def test_home(self):
        response = self.client.get(reverse('blogs-home'))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('blogs-frontship'))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('blogs-dashboard-2'))
        self.assertEqual(response.status_code, 200)



        


