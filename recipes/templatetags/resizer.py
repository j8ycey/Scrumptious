from django import template

register = template.Library()


def resize_to(ingredient, target):
    servings = ingredient.recipe.servings
    if servings is not None and target is not None:
        try:
            ratio = int(target) / servings
            return ingredient.amount * ratio
        except ValueError:
            pass
    return ingredient.amount


register.filter(resize_to)
