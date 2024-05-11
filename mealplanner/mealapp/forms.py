from django import forms
from .models import Meal, MealItem

class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ['name']

class MealItemForm(forms.ModelForm):
    class Meta:
        model = MealItem
        fields = ['name']