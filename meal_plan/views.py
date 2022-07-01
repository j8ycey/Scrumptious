from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.

from meal_plan.models import MealPlan


class MealPlanListView(LoginRequiredMixin, ListView):
    model = MealPlan
    template_name = "meal_plan/list.html"
    context_object_name = "meal_plan"

    def get_queryset(self):
        return MealPlan.objects.filter(owner=self.request.user)


class MealPlanDetailView(UserPassesTestMixin, DetailView):
    model = MealPlan
    template_name = "meal_plan/detail.html"
    context_object_name = "meal_plan"

    def test_func(self):
        return self.request.user == self.get_object().owner


class MealPlanCreateView(LoginRequiredMixin, CreateView):
    model = MealPlan
    template_name = "meal_plan/new.html"
    fields = ["name", "date", "recipes"]

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy("meal_plan_detail", kwargs={"pk": self.object.pk})


class MealPlanUpdateView(UserPassesTestMixin, UpdateView):
    model = MealPlan
    template_name = "meal_plan/edit.html"
    fields = ["name", "date", "recipes"]

    def get_success_url(self):
        return reverse_lazy("meal_plan_detail", kwargs={"pk": self.object.pk})
    
    def test_func(self):
        return self.request.user == self.get_object().owner


class MealPlanDeleteView(UserPassesTestMixin, DeleteView):
    model = MealPlan
    template_name = "meal_plan/delete.html"
    success_url = reverse_lazy("meal_plan_list")
    context_object_name = "meal_plan"

    def test_func(self):
        return self.request.user == self.get_object().owner
