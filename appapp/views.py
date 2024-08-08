from django.shortcuts import render

from .models import Ingredient, Recipe

def ingredient_list(request):
    ingredients = Ingredient.objects.all()
    return render(request, 'appapp/ingredient_list.html', {'ingredients': ingredients})

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'appapp/recipe_list.html', {'recipes': recipes})

def ingredient_detail(request, pk):
    ingredient = Ingredient.objects.get(id=pk)
    return render(request, 'appapp/ingredient_detail.html', {'ingredient': ingredient})

def recipe_detail(request, pk):
    recipe = Recipe.objects.get(id=pk)
    return render(request, 'appapp/recipe_detail.html', {'recipe': recipe})

