from django.db import models

class User(models.Model):
    email = models.CharField(max_length=50)
    username = models.CharField(max_length=25)
    recpies = models.ForeignKey("Recipe", on_delete=models.CASCADE, blank=True, null=True)
    ratings = models.ForeignKey("Rating", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.username

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    ingredients = models.ManyToManyField("Ingredient")
    rating = models.ForeignKey("Rating", on_delete=models.SET_NULL, related_name="Rating", null=True, blank=True)

    def __str__(self):
        return self.name

class Rating(models.Model):
    stars = models.IntegerField()
    left_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="Recipe")

class Ingredient(models.Model):
    name = models.CharField(max_length=25)
    icon = models.ImageField()
    used_in = models.ForeignKey(Recipe, on_delete=models.RESTRICT, blank=True, null=True)

    def __str__(self):
        return self.name
    
class Photo(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    url = models.CharField(max_length=200)

    def __str__(self):
        return f"Photo for ingredient_icon: {self.ingredient_id} @{self.url}"

