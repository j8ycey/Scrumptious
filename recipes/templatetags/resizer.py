from django import template
register = template.Library()


# def resize_to(ingredient, desired_servings):
#     sesrvings = ingredient.recipe.servings
#     ratio = desired_servings / sesrvings
#     resized_amount = ingredient.amount * ratio
#     return resized_amount

def resize_to(ingredient, target):
    num_servings = ingredient.recipe.servings
    if num_servings is not None and target is not None:
        ratio = int(target) / num_servings
        return ratio * ingredient.amount
    return ingredient.amount


register.filter(resize_to)
