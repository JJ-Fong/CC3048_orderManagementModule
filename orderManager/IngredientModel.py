import uuid 
import datetime

class IngredientModel:
    ingredient_guid = str(uuid.uuid4())
    name = ""
    qty = 0

    def __init__(self, ingredient):
        for key,value in ingredient.items():
            if (key == 'name'):
                self.name = value
            elif (key == 'qty'):
                self.qty = value 

    def ValidateIngredient(self, ingredient):
        if ingredient.name == None or ingredient.name == "":
            raise Exception("Ingredient NAME is invalid")
        if ingredient.qty == None or ingredient.qty < 0:
            raise Exception("Ingredient QTY is invalid")
        return True
