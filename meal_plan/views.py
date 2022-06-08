from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

from meal_plan.forms import MealPlanForm
from meal_plan.models import USER_MODEL, MealPlan


class MealPlanListView(LoginRequiredMixin, ListView):
    model = MealPlan
    template_name = "meal_plan/list.html"
    paginate_by = 6


class MealPlanDetailView(LoginRequiredMixin, DetailView):
    model = MealPlan
    template_name = "meal_plan/detail.html"


class MealPlanCreateView(LoginRequiredMixin, CreateView):
    model = MealPlan
    template_name = "meal_plan/new.html"
    fields = ["name", "date", "recipes"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy("meal_plan_detail", kwargs={"pk": self.object.pk})


class MealPlanUpdateView(LoginRequiredMixin, UpdateView):
    model = MealPlan
    template_name = "meal_plan/edit.html"
    fields = ["name", "date", "recipes"]

    def get_success_url(self):
        return reverse_lazy("meal_plan_detail", kwargs={"pk": self.object.pk})


class MealPlanDeleteView(LoginRequiredMixin, DeleteView):
    model = MealPlan
    template_name = "meal_plan/delete.html"
    
    def get_success_url(self):
        return reverse_lazy("meal_plan_detail", kwargs={"pk": self.object.pk})

