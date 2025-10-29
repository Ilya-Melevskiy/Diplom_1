import pytest

from practicum.ingredient import Ingredient
from practicum import ingredient_types


class TestIngredient:

    @pytest.mark.parametrize('type', [ingredient_types.INGREDIENT_TYPE_FILLING, 
                                      ingredient_types.INGREDIENT_TYPE_SAUCE])
    def test_ingredient_init_correct_data_create_ingredient_correct_type(self, type):
        ingredient = Ingredient(type, 'мясо', 100.5)
        assert ingredient.type == type

    @pytest.mark.parametrize('name', ['сыр', 'мясо', 'бекон'])
    def test_ingredient_init_correct_data_create_ingredient_correct_name(self, name):
        ingredient = Ingredient('начинка', name, 100.5)
        assert ingredient.name == name

    @pytest.mark.parametrize('price', [10.0, 123.45, 1500.1])
    def test_ingredient_init_correct_data_create_ingredient_correct_price(self, price):
        ingredient = Ingredient('начинка', 'мясо', price)
        assert ingredient.price == price

    def test_get_price_return_correct_price(self, ingredient):
        assert ingredient.get_price() == 100.5

    def test_get_price_return_correct_name(self, ingredient):
        assert ingredient.get_name() == 'мясо'

    def test_get_price_return_correct_type(self, ingredient):
        assert ingredient.get_type() == ingredient_types.INGREDIENT_TYPE_FILLING
