import uuid 

class DetailModel:
    detail_guid = str(uuid.uuid4())
    order_guid = ""
    product_guid = ""
    qty = 0.0
    value = 0.0 

    def __init__(self, duple):
        detail, order_guid = duple
        self.order_guid = order_guid
        for key,value in detail.items():
            if (key == 'product'):
                self.product_guid = value
            elif (key == 'qty'):
                self.qty = value 

    def ValidateDetail(self, detail):
        if detail.name == None or detail.name == "":
            raise Exception("detail NAME is invalid")
        if detail.qty == None or detail.qty < 0:
            raise Exception("detail QTY is invalid")
        return True

    def toString(self):
        print self.detail_guid
        print self.order_guid
        print self.product_guid
        print self.qty
        print self.value