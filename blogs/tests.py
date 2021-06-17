from django.test import TestCase

# Create your tests here.
from .models import shipd

import datetime

# Create your tests here.
class hello(TestCase):
    def test_page_is_created_successfully(self):
        a1d=datetime.date(2021,6,3)
        a1=shipd(shipid=1,shname='MCP-101',shorig='Miami',shdest='Cape Town',shdate=a1d,con_e=0,con_f=0,con_s=0)
        a1.save()