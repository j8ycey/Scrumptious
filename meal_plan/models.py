from django.db import models
from django.conf import settings


USER_MODEL = settings.AUTH_USER_MODEL

# Create your models here.


class MealPlan(models.Model):
    name = models.CharField(max_length=120)
    date = models.DateField(null=True)
    owner = models.ForeignKey(
      USER_MODEL,
      related_name="meal_plans",
      on_delete=models.CASCADE,
    )
    recipes = models.ManyToManyField("recipes.Recipe", related_name="meal_plan")

    def __str__(self):
        return "Meal Plan: " + self.name


# str(MealPlan.owner.)