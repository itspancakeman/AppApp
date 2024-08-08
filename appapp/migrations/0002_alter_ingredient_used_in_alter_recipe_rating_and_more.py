# Generated by Django 5.0.8 on 2024-08-08 03:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='used_in',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.RESTRICT, to='appapp.recipe'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='rating',
            field=models.ManyToManyField(blank=True, related_name='Rating', to='appapp.rating'),
        ),
        migrations.AlterField(
            model_name='user',
            name='ratings',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='appapp.rating'),
        ),
        migrations.AlterField(
            model_name='user',
            name='recpies',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='appapp.recipe'),
        ),
    ]
