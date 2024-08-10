from django.urls import path
from . import views
from django.conf.urls import include
from django.contrib import admin

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
    path('recipes/<int:pk>/delete', views.recipe_delete, name='recipe_delete'),
    path('ratings/new', views.rating_create, name='rating_create'),
    path('ratings', views.rating_list, name='rating_list'),
    path('users/new', views.user_create, name='user_create'),
    path('', views.home_page, name='home_page'),
    path('ingredients/<int:pk>/add_photo', views.add_photo, name='add_photo'),
    path('admin/', admin.site.urls),
]