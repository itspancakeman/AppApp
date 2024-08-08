from django.db import models

class User(models.Model):
    email = models.CharField(max_length=50)
    username = models.ChardField(max_length=25)
    recpies = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ratings = models.ForeignKey(Rating, on_delete=models.SET_NULL)

    def __str__(self):
        return self.username

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL)
    ingredients = models.ManyToManyField(Ingredient)
    ratings = models.ManyToManyField(Rating)

    def __str__(self):
        return self.name

class Rating(models.Model):
    stars = models.IntegerField(max_length=5)
    left_by = models.ForeignKey(User, on_delete=models.SET_NULL)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

class Ingredient(models.Model):
    name = models.CharField(max_length=25)
    icon = models.ImageField()
    used_in = models.ForeignKey(Recipe, on_delete=models.RESTRICT)

    def __str__(self):
        return self.name