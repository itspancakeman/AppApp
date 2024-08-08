from django.urls import path
from . import views

urlpatterns = [
    path('ingredients', views.ingredient_list, name='ingredient_list'),
    path('ingredients/<int:pk>', views.ingredient_detail, name='ingredient_detail'),
    path('recipes', views.recipe_list, name='recipe_list'),
    path('recipes/<int:pk>', views.recipe_detail, name='recipe_detail'),
]