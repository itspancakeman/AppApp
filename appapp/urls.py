from django.urls import path
from . import views

urlpatterns = [
    path('ingredients', views.ingredient_list, name='ingredient_list'),
    path('ingredients/<int:pk>', views.ingredient_detail, name='ingredient_detail'),
    path('recipes', views.recipe_list, name='recipe_list'),
    path('recipes/<int:pk>', views.recipe_detail, name='recipe_detail'),
    path('ingredients/new', views.ingredient_create, name='ingredient_create'),
    path('recipes/new', views.recipe_create, name='recipe_create'),
    path('ingredients/<int:pk>/edit', views.ingredient_edit, name='ingredient_edit'),
    path('recipes/<int:pk>/edit', views.recipe_edit, name='recipe_edit'),
    path('ingredients/<int:pk>/delete', views.ingredient_delete, name='ingredient_delete'),
]