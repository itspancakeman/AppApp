# Generated by Django 5.1 on 2024-08-10 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appapp', '0004_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='icon',
            new_name='ingredient',
        ),
    ]
