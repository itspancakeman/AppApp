from django.contrib import admin
from appapp.models import User, Recipe, Rating, Ingredient, Photo

admin.site.register(User)
admin.site.register(Recipe)
admin.site.register(Rating)
admin.site.register(Ingredient)
admin.site.register(Photo)
