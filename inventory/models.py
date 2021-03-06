from django.db import models
from decimal import *
# Create your models here.
class Ingredient(models.Model):
    OUNCE = 'oz'
    POUND = 'lb'
    UNIT_CHOICES = [
        (OUNCE,'ounce'),
        (POUND, 'pound')
    ]
    name = models.CharField(max_length=20)
    unit = models.CharField(max_length=2, choices=UNIT_CHOICES, default="oz")
    availableQuantity = models.IntegerField(default=10)
    unitPrice = models.DecimalField(max_digits=10, decimal_places=2)

    def get_absolute_url(self):
        return "/inventory"
    def __str__(self):
        return self.name

class MenuItem(models.Model):
    title = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=11.50)

    def sum_recipe_prices(self):#this totals the ingredient COST of each menu item, not the price.
        theTotalPrice = Decimal(0.00)
        theListOfIngredients = self.reciperequirement_set.all()
        for ing in theListOfIngredients:
            theTotalPrice += ing.ingredient_cost
        return theTotalPrice

    def get_absolute_url(self):
        return "/menu"
    def __str__(self):
        return f"{self.title}"

class Purchase(models.Model):
    date = models.DateField(auto_now=True)
    menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return f"/purchase/{self.id}/confirm"
    def __str__(self):
        return f"{self.id} {self.menuitem} {self.date}"
        #define quantity of each ingredient needed: menuitem.REcReq_set(all).quantyty
        #define how much of each ingredient is available: menuitem.REcReq.availableQuantity


class RecipeRequirement(models.Model):
    menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=3, decimal_places=0, default=1)
    @property#calculate cost of ingredient amount used in recipe
    def ingredient_cost(self):
        return self.ingredient.unitPrice * self.quantity

    def get_absolute_url(self):
        return "/menu"
    def __str__(self):
        return f"{self.id} {self.menuitem} {self.ingredient} {self.quantity} {self.ingredient_cost}"
