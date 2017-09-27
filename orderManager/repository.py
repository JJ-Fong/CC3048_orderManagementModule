from models import Client, Order, Recipe, OrderDetail, Ingredient
from django.db import IntegrityError

def CreateNewClient(client):
	try:
		client_model = Client.objects.create_new_client(client)
		return client_model
	except IntegrityError as e:
		err = e.message.encode('utf-8')
		raise Exception(err)


def FindQtyOfIngredientByRecipeGui(guid):
    try:
        ing = Ingredient.objects.get_ingredient_qty(guid)
        return ing
    except:
		# raise Exception("Invalid ingredient, there is no ingredient with dat recipe guid.. biatch.")
		ing = 0
		return ing

def UpdateQtyOfIngredientByRecipeGui(guid,cant):
    try:
        ing = Ingredient.objects.update_ingredient_qty(guid,cant)
        # return ing
    except:
		raise Exception("Guess what? Error! Can't you even make an update? u suck..")

def FindPriceInRecipe(guid):
	try:
		precio = Recipe.objects.find_price_in_recipe_by_guid(guid)
		return precio
	except:
		# raise Exception("There is no price for this product.")
		precio = 0.0
		return precio

def CreateNewOrder(order):
	try:
		order_model = Order.objects.create_new_order(order)
		return order_model
	except IntegrityError as e:
		err = e.message.encode('utf-8')
		raise Exception(err)

def CreateNewDetail(detail):
	try:
		detail_model = OrderDetail.objects.create_new_order_detail(detail)
		return detail_model
	except IntegrityError as e:
		err = e.message.encode('utf-8')
		raise Exception(err)


def GetRecipeIngredients(recipe):
	try:
		ingredients = Ingredient.objects.find_ingredient_by_recipe_guid(recipe)
		return ingredients
	except IntegrityError as e:
		err = e.message.encode('utf-8')
		raise Exception(err)


def GetRecipeGuid(recipe_name):
	try:
		recipe = Recipe.objects.find_guid_by_name(recipe_name)
		return recipe
	except IntegrityError as e:
		err = e.message.encode('utf-8')
		raise Exception(err)
