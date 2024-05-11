from django.shortcuts import render, redirect
from .models import Meal, MealItem
from .forms import MealForm, MealItemForm

def remove_all_meals(request):
    Meal.objects.all().delete()
    return redirect('mealapp:meals')

def index(request):
    if request.method == 'POST':
        form = MealForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mealapp:meals')
    else:
        form = MealForm()
    return render(request, 'mealapp/index.html', {'form': form})

def meals(request):
    meals = Meal.objects.all()
    context = {'meals': meals}
    return render(request, 'mealapp/meals.html', context)

def meal(request, meal_id):
    meal = Meal.objects.get(id=meal_id)

    if request.method == 'POST':
        form = MealItemForm(request.POST)
        if form.is_valid():
            meal_item = form.save(commit=False)
            meal_item.meal = meal
            meal_item.save()
            return redirect('mealapp:meal', meal_id=meal_id)
    else:
        form = MealItemForm()
    
    meal_items = meal.mealitem_set.all()

    context = {'meal': meal, 'meal_items': meal_items, 'item_form': form}
    
    return render(request, 'mealapp/meal.html', context)
