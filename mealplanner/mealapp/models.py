from django.db import models

class Meal(models.Model):
    name = models.CharField(max_length=100)

    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class MealItem(models.Model):
    name = models.CharField(max_length=100)

    meal = models.ForeignKey(Meal, on_delete = models.CASCADE)

    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name 