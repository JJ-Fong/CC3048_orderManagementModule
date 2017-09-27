from django.test import TestCase
from .service import *
from .OrderModel import *
from .RecipeModel import *
from .IngredientModel import *
from .models import *
import json 
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

		self.assertTrue(True) 