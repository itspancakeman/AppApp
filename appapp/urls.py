from django.urls import path
from . import views

urlpatterns = [
    path('ingredients/<int:pk>', views.ingredient_list, name='ingredient_list'),
    path('recipes/<int:pk>', views.recipe_list, name='recipe_list'),
]