import uuid 
import datetime

class RecipeModel:
    recipe_guid = str(uuid.uuid4())
    name = ""
    price = 0.0
    ingredients = []

    def __init__(self, recipe):
        for key,value in recipe.items():
            if (key == 'name'):
                self.name = value
            elif (key == 'price'):
                self.price = value 
            elif (key == 'ingredients'):
                self.ingredients  = value

    def ValidateRecipe(self, recipe):
        if recipe.name == None or recipe.name == "":
            raise Exception("Recipe NAME is invalid")
        if recipe.price == None or recipe.price < 0:
            raise Exception("Recipe PRICE is invalid")
        if recipe.ingredients == None:
            rause Exception("Recipe INGREDIENTS is invalid")
        return True 
