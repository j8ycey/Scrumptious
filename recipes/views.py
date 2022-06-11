from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from recipes.forms import RatingForm
from recipes.models import Recipe, ShoppingItem, FoodItem


def log_rating(request, recipe_id):
    try:
        if request.method == "POST":
            form = RatingForm(request.POST)
            if form.is_valid():
                rating = form.save(commit=False)
                rating.recipe = Recipe.objects.get(pk=recipe_id)
                rating.save()
        return redirect("recipe_detail", pk=recipe_id)
    except Recipe.DoesNotExist:
        return redirect("recipes_list")


class RecipeListView(ListView):
    model = Recipe
    template_name = "recipes/list.html"
    paginate_by = 8

    def get_queryset(self):
        querystring = self.request.GET.get("q")
        if querystring is None:
            querystring = ""
        return Recipe.objects.filter(description__icontains=querystring)


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipes/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["rating_form"] = RatingForm()
        food_list = []
        for item in self.request.user.shopping_items.all():
            food_list.append(item.food_item)

        context["food_list"] = food_list
        context["servings"] = self.request.GET.get("servings")
        return context


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = "recipes/new.html"
    fields = ["name", "description", "image", "servings"]
    success_url = reverse_lazy("recipes_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class RecipeUpdateView(LoginRequiredMixin, UpdateView):
    model = Recipe
    template_name = "recipes/edit.html"
    fields = ["name", "description", "image", "servings"]
    success_url = reverse_lazy("recipes_list")


class RecipeDeleteView(LoginRequiredMixin, DeleteView):
    model = Recipe
    template_name = "recipes/delete.html"
    success_url = reverse_lazy("recipes_list")

# __________________________________________________________


class ShoppingItemsList(LoginRequiredMixin, ListView):
    model = ShoppingItem
    template_name = "cart/list.html"
    context_object_name = "shopping_list"
    login_url = "/login/"

    def get_queryset(self):
        return ShoppingItem.objects.filter(user=self.request.user)

@login_required(login_url="/login")
def create_shopping_item(request, pk, recipe_id):
    """purpose is to create an entry in the database specifically a shopping item entry and redirect you elsewhere"""
    if request.method == "POST" and pk:
        item = ShoppingItem(
            user=request.user,
            food_item=FoodItem.objects.get(pk=pk)
        )
        item.save()
        return redirect("recipe_detail", pk=recipe_id)
    else:
        return redirect("recipe_list")


@login_required(login_url="/login")
def shopping_list_delete(request):
    ShoppingItem.objects.filter(user=request.user).delete()
    return redirect("shopping_list")
