from models import Client, Recipe, Order, Ingredient, OrderDetail
from OrderModel import *
from repository import *

def HandleOrderRequest(order):
	if order == {}:
		raise Exception("Invalid order data")
	orderModel = OrderModel(order)
	order_model = CreateNewOrder(orderModel)
	products = []
	ingredients = []

  	for det in orderModel.detail:
		detail_model = CreateNewDetail(det)
		products.append(det.product_guid)
	
	for p in products:
		p_guid = GetRecipeGuid(p)
		p_ingredients = GetRecipeIngredients(p_guid)
		for ing in p_ingredients:
			ingredients.append(ing)

	response = {}
	response['token'] = order['token']
	response['store'] = 'Tienda01'
	response['order'] = orderModel.order_guid
	response['ingredients'] = ingredients
	return response

def ValidateOrderRequest(order):
	json_to_return = "{nit:c/f,"
	respond = False
	cont = 0
	if order == {}:
		raise Exception("Invalid order data")
	for i,elem in order.items():
		cont += 1
		total = 0.0
		if((i == "token" or i == "user") or (i == "order" or i == "orderid")):
			json_to_return = json_to_return + i + ":" + elem + ","
		if (i == "products"):
			#validacion de que la orden tenga al menos un ingrediente
			allprods = elem
			if(len(elem) > 0):
				print i,elem
				for j in elem:
					id_ing = j["product_guid"]
					cant = j["quantity"]
					precio = FindPriceInRecipe(id_ing)
					total = total + (precio*cant)
					#update cantidad de acuerdo al ID del ingrediente
					qty_by_ing = FindQtyOfIngredientByRecipeGui(id_ing)
					print qty_by_ing,cant
					print "precio",precio
					print "total",total
					if(qty_by_ing >= cant):
						#si hay suficientes ingredientes
						respond = True
						UpdateQtyOfIngredientByRecipeGui(qty_by_ing - cant) #update de cantidad de ingredientes.
					else:
						print "No hay suficientes ingredientes para preparar la orden."

			else:
				print "Products in order has no ingredients"

		if(cont == len(order)):
			json_to_return = json_to_return + "amount:"+str(total) + "," + "products:" + str(allprods) + "}"
			print "JSON!",json_to_return
				
	if (respond):
		# order = '{"nit":"5464646-3","token" : "df6d11e18af84c7eb3bbcc8b7d7a9e47","orderid" : "lfakjsdlfkajsdf","amount":100.52}'
		print json_to_return
		return json_to_return
	else:
		return ""
