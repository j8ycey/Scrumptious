# Generated by Django 4.0.3 on 2022-06-10 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0008_shoppingitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='servings',
            field=models.PositiveIntegerField(null=True),
        ),
    ]