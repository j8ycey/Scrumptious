from django.contrib import admin
from meal_plan.models import MealPlan

# Register your models here.


class MealPlanAdmin(admin.ModelAdmin):
    pass


admin.site.register(MealPlan, MealPlanAdmin)
