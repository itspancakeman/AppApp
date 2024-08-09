from django import forms
from .models import Ingredient, Recipe

class IngredientForm(forms.ModelForm):

    class Meta:
        model = Ingredient
        fields = ('name', 'icon', 'used_in')