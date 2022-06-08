from django.urls import path
from django.contrib.auth import views as auth_views

from meal_plan.views import (
    MealPlanCreateView,
    MealPlanDeleteView,
    MealPlanUpdateView,
    MealPlanDetailView,
    MealPlanListView,

)

urlpatterns = [
  path("", MealPlanListView.as_view(), name="meal_plan_list"),
  path("<int:pk>/", MealPlanDetailView.as_view(), name="meal_plan_detail"),
  path("<int:pk>/delete/", MealPlanDeleteView.as_view(), name="meal_plan_delete"),
  path("new/", MealPlanCreateView.as_view(), name="meal_plan_new"),
  path("<int:pk>/edit/", MealPlanUpdateView.as_view(), name="meal_plan_edit"),

  path("accounts/login", auth_views.LoginView.as_view(), name="login"),
  path("accounts/logout", auth_views.LogoutView.as_view(), name="logout"),
]
