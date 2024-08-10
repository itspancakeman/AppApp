from django.shortcuts import render, redirect

from .forms import IngredientForm, RecipeForm, RatingForm, UserForm

from .models import Ingredient, Recipe, Rating, User, Photo

import uuid
import boto3

S3_BASE_URL = 'https://s3.us-east-2.amazonaws.com/'
BUCKET = 'appappstorage'

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

def recipe_edit(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            recipe = form.save()
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'appapp/recipe_create.html', {'form': form})

def ingredient_delete(request, pk):
    Ingredient.objects.get(id=pk).delete()
    return redirect('ingredient_list')

def recipe_delete(request, pk):
    Recipe.objects.get(id=pk).delete()
    return redirect('recipe_list')

def rating_create(request):
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save()
            return redirect ('recipe_list', pk=rating.pk)
    else:
        form = RatingForm()
    return render(request, 'appapp/rating_create.html', {'form': form})

def rating_list(request):
    ratings = Rating.objects.all()
    return render(request, 'appapp/rating_list.html', {'ratings': ratings})

def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('user_details', pk=user.pk)
    else:
        form = UserForm()
    return render(request, 'appapp/user_create.html', {'form': form})

def home_page(request):
    return render(request, 'appapp/home_page.html')

def add_photo(request, pk):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            Photo.objects.create(url=url, pk=photo_file.pk)
        except:
            print('An error occured uploading file to S3')
    return redirect('ingredient_detail', pk=photo_file.pk)

