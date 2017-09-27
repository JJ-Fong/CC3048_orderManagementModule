import uuid
from DetailModel import * 

class OrderModel:
	order_guid = str(uuid.uuid4())
	address = ""
	status = "" 
	store = ""
	client = None 

	def __init__(self, order):
		self.detail = []
		for k, v in order.items():
			if k == 'order': 	
				for key, value in v.items():
					key = key.encode('utf-8')
					if (key == 'address'):
						self.address = value
					if (key == 'products'):
						for product in value:
							detInfo = (product, self.order_guid)
							detailModel = DetailModel(detInfo)
							self.detail.append(detailModel)	
					if (key == 'store'):
						self.store = value
					if (key == 'status'):
						self.status = value
					
	def ValidateOrder(self, order):
		if order.client == None or order.client == "":
			raise Exception("Order CLIENT is invalid")
		if order.products == None or order.products == "":
			raise Exception("Order PRODUCTS is invalid")
		if order.status == None or order.status == "":
			raise Exception("Order STATUS is invalid")	
		return True 
	

