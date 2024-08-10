from django import forms
from .models import Ingredient, Recipe, Rating, User

class IngredientForm(forms.ModelForm):

    class Meta:
        model = Ingredient
        fields = ('name', 'icon', 'used_in')

class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = ('name', 'created_by', 'ingredients')

class RatingForm(forms.ModelForm):

    class Meta:
        model = Rating
        fields = ('stars', 'left_by', 'recipe')

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('email', 'username')

