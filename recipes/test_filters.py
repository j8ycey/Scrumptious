from ctypes import resize
from unittest import TestCase

from recipes.models import Ingredient, Recipe
from recipes.templatetags.resizer import resize_to


# def resize_to(ingredient, target):
#     servings = ingredient.recipe.servings
#     if servings is not None and target is not None:
#         try:
#             ratio = int(target) / servings
#             return ingredient.amount * ratio
#         except ValueError
#             pass
#     return ingredient.amount


class ResizeToTests(TestCase):
    def test_no_resize(self):
        # Arrange

        # Act

        # Assert
        with self.assertRaises(AttributeError):
            resize_to(None, 3)
        # assertRaises checks to see if error is raised

    def test_recipe_has_no_serving(self):
        # Arrange
        recipe = Recipe(servings=None)
        ingredient = Ingredient(recipe=recipe, amount=5)

        # Act
        result = resize_to(ingredient, None)

        # Assert
        self.assertEqual(5, result)
        # assertEqual checks to see if those values are returned

    def test_resize_to_is_none(self):
        # Arrange
        recipe = Recipe(servings=2)
        ingredient = Ingredient(recipe=recipe, amount=5)

        # Act
        result = resize_to(ingredient, None)

        # Assert
        self.assertEqual(5, result)

    def test_values_for_servings_amount_and_target(self):
        # Arrange
        recipe = Recipe(servings=2)
        ingredient = Ingredient(recipe=recipe, amount=5)
        
        # Act
        result = resize_to(ingredient, 10)
        
        # Assert
        self.assertEqual(25, result)

    def test_target_is_letters(self):
        # Arrange
        recipe = Recipe(servings=2)
        ingredient = Ingredient(recipe=recipe, amount=5)
        # Act
        result = resize_to(ingredient, "abc")
        # Assert
        self.assertEqual(5, result)
