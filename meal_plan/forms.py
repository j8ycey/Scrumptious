from django import forms
from meal_plan.models import MealPlan


class MealPlanForm(forms.ModelForm):
    class Meta:
        model = MealPlan
        fields = [
            "name",
            "author",
            "description",
            "image",
        ]

