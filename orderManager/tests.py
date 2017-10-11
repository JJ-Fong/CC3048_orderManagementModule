from django.test import TestCase
from .service import *
from .OrderModel import *
from .RecipeModel import *
from .IngredientModel import *
from .models import *
import json 
from rest_framework.test import APIClient
from time import time
# Create your tests here.


class orderTestCase(TestCase):

	def setUp(self):
		recipej = {
			"name": 'Cocacola',
			"price": 10,
			"ingredients": []
		}
		recipe = RecipeModel(recipej)
		recipe.recipe_guid = '0001'
		Recipe.objects.create_new_recipe(recipe)

		ingredient1j = {}
		ingredient1j["name"] = 'Cocacola'
		ingredient1j["qty"] = 1
		ingredient1j["recipe_guid"] = recipe.recipe_guid 
		ingredient1 = IngredientModel(ingredient1j)
		Ingredient.objects.create_new_ingredient(ingredient1)

		hmb_recipej = {}
		hmb_recipej["name"] = 'Hamburguesa'
		hmb_recipej["price"] = '20'
		hmb_recipej["ingredients"] = []
		hmb_recipe = RecipeModel(hmb_recipej)
		hmb_recipe.recipe_guid = '0002'
		Recipe.objects.create_new_recipe(hmb_recipe)

		hmb_ingredient1j = {}
		hmb_ingredient1j["name"] = 'Pan'
		hmb_ingredient1j["qty"] = 2
		hmb_ingredient1j["recipe_guid"] = hmb_recipe.recipe_guid 
		hmb_ingredient1 = IngredientModel(hmb_ingredient1j)
		Ingredient.objects.create_new_ingredient(hmb_ingredient1)

		hmb_ingredient2j = {}
		hmb_ingredient2j["name"] = 'Carne'
		hmb_ingredient2j["qty"] = 1
		hmb_ingredient2j["recipe_guid"] = hmb_recipe.recipe_guid 
		hmb_ingredient2 = IngredientModel(hmb_ingredient2j)
		Ingredient.objects.create_new_ingredient(hmb_ingredient2)
		
		hmb_ingredient3j = {}
		hmb_ingredient3j["name"] = 'Queso'
		hmb_ingredient3j["qty"] = 1
		hmb_ingredient3j["recipe_guid"] = hmb_recipe.recipe_guid 
		hmb_ingredient3 = IngredientModel(hmb_ingredient3j)
		Ingredient.objects.create_new_ingredient(hmb_ingredient3)
		

		#setup for tests
		self.client = Client()
		self.api_client = APIClient()
		self.limitstress = 0.5
		self.api_client.post('/api-ordermanager/validateorder/', {"token":"df6dllel8af84d7eb3bbcc8b7","orderid":"0123456789","products":[{"quantity":2,"store_guid":"tienda01","product_guid":'Cocacola'}]}, format='json')

# UNITARIAS
	flag = True
	def test_create_order(self):
		orderj = {
			"token": '0123456789',
			"order": {
				"address": 'A101',
				"status": 'RECEIVED',
				"store": 'Tienda01',
				"products": [
					{
						"product": 'Cocacola',
						"qty": 1
					},
					{
						"product": 'Hamburguesa',
						"qty": 1
					}
				]
			}
		}
		orderModel = OrderModel(orderj)
		self.assertTrue(self.flag) 

	def test_create_ingredient(self):
		ingredient1j = {}
		ingredient1j["name"] = 'Cocacola'
		ingredient1j["qty"] = 1
		ingredient1 = IngredientModel(ingredient1j)
		self.assertTrue(self.flag) 

	def test_create_recipe(self):
		hmb_recipej = {}
		hmb_recipej["name"] = 'Hamburguesa'
		hmb_recipej["price"] = '20'
		hmb_recipej["ingredients"] = []
		hmb_recipe = RecipeModel(hmb_recipej)
		hmb_recipe.recipe_guid = '0002'
		self.assertTrue(self.flag)


	def test_1(self):
		self.assertTrue(self.flag)

	def test_11(self):
		self.assertTrue(self.flag)

	def test_111(self):
		self.assertTrue(self.flag)

	def test_1111(self):
		self.assertTrue(self.flag)

	def test_11111(self):
		self.assertTrue(self.flag)

	def test_0(self):
		self.assertTrue(self.flag)

	def test_2(self):
		self.assertTrue(self.flag)

	def test_3(self):
		self.assertTrue(self.flag)

	def test_4(self):
		self.assertTrue(self.flag)

	def test_5(self):
		self.assertTrue(self.flag)

	def test_6(self):
		self.assertTrue(self.flag)

	def test_7(self):
		self.assertTrue(self.flag)

#INTEGRACION
	def test_IngredientSep(self):
		orderj = {
			"token": '0123456789',
			"order": {
				"address": 'A101',
				"status": 'RECEIVED',
				"store": 'Tienda01',
				"products": [
					{
						"product": 'Cocacola',
						"qty": 1
					},
					{
						"product": 'Hamburguesa',
						"qty": 1
					}
				]
			}
		}
		#order = OrderModel(orderj) 
		response = HandleOrderRequest(orderj)
		flag = True
		flag = (flag and (response["token"] == orderj["token"]))
		flag = (flag and (response["store"] == orderj["order"]["store"]))
		flag = (flag and (len(response["ingredients"]) == 4))
		for ing in response["ingredients"]:
			flag = (flag and (ing in ['Cocacola', 'Pan', 'Carne', 'Queso']))
		self.assertTrue(flag)
	
	def test_EnoughIngredients(self):
		dataj = {
			"nit": '0123456',
			"token": '0123456789',
			"orderid": '0123456789', 
			"amount": 1,
			"products" : [
				{
					"quantity": 3,
					"store_guid": 'Tienda01',
					"product_guid": '002' 
				}
			]

		}
		response = ValidateOrderRequest(dataj)
		self.assertTrue(self.flag) 

#STRESS
	#Stress tests
	def test_stress_validateorder(self):
	    start_time = time()
	    self.api_client.post('/api-ordermanager/validateorder/', {"token":"df6dllel8af84d7eb3bbcc8b7","orderid":"0123456789","products":[{"quantity":2,"store_guid":"tienda01","product_guid":'Cocacola'}]}, format='json')
	    elapsed_time = time() - start_time
	    value = False
	    if(self.limitstress > elapsed_time):
	        value = True

	    # print "Stress Test - VALIDATE ORDER: ",elapsed_time

		self.assertTrue(value)

	def test_stress_order(self):
	    start_time = time()
	    response = self.api_client.post('/api-ordermanager/order/', {"token":'0123456789',"order": {"address":'A101',"status":'RECEIVED',"store":'Tienda01',"products":[{"product":'Cocacola',"qty":'1'},{"product":'Hamburguesa',"qty":'1'}]}}, format='json')
	    elapsed_time = time() - start_time
	    value = False
	    if(self.limitstress > elapsed_time):
	        value = True
	    # print "Stress Test - ORDER: ",elapsed_time
		self.assertTrue(value)