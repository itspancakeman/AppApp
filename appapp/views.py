from django.shortcuts import render, redirect

from .forms import IngredientForm, RecipeForm

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

def ingredient_create(request):
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            ingredient = form.save()
            return redirect('ingredient_detail', pk=ingredient.pk)
    else:
        form = IngredientForm()
    return render(request, 'appapp/ingredient_create.html', {'form': form})

def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save()
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = RecipeForm()
    return render(request, 'appapp/recipe_create.html', {'form': form})

def ingredient_edit(request, pk):
    ingredient = Ingredient.objects.get(pk=pk)
    if request.method == 'POST':
        form = IngredientForm(request.POST, instance=ingredient)
        if form.is_valid():
            ingredient = form.save()
            return redirect('ingredient_detail', pk=ingredient.pk)
    else:
        form = IngredientForm(instance=ingredient)
    return render(request, 'appapp/ingredient_create.html', {'form': form})

