# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.test.utils import setup_test_environment
from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient


from models import *
from time import time
#from  UserModel import *
from service import *

def setUp (self):
	self.client = Client()
	self.api_client = APIClient()
	self.limitstress = 0.5
	self.api_client.post('/api-ordermanager/validateorder/', {"token":"df6dllel8af84d7eb3bbcc8b7","orderid":"0123456789","products":[{"quantity":2,"store_guid":"tienda01","product_guid":'Cocacola'}]}, format='json')

#Stress tests
def stresstest_validateorder(self):
    start_time = time()
    self.api_client.post('/api-ordermanager/validateorder/', {"token":"df6dllel8af84d7eb3bbcc8b7","orderid":"0123456789","products":[{"quantity":2,"store_guid":"tienda01","product_guid":'Cocacola'}]}, format='json')
    elapsed_time = time() - start_time
    value = False
    if(self.limitstress > elapsed_time):
        value = True

    print "Stress Test - VALIDATE ORDER: ",elapsed_time

	self.assertTrue(value)

def stresstest_order(self):
    start_time = time()
    response = self.api_client.post('/api-ordermanager/order/', {"token":'0123456789',"order": {"address":'A101',"status":'RECEIVED',"store":'Tienda01',"products":[{"product":'Cocacola',"qty":'1'},{"product":'Hamburguesa',"qty":'1'}]}}, format='json')
    elapsed_time = time() - start_time
    value = False
    if(self.limitstress > elapsed_time):
        value = True
    print "Stress Test - ORDER: ",elapsed_time
	self.assertTrue(value)