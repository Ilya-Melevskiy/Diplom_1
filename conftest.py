import pytest

from practicum.bun import Bun 
from practicum.ingredient import Ingredient
from practicum import ingredient_types
from practicum.database import Database
from practicum.burger import Burger

@pytest.fixture
def bun():
    bun = Bun('Булка', 7.2)
    return bun

@pytest.fixture
def ingredient():
    ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_FILLING, 'мясо', 100.5)
    return ingredient

@pytest.fixture
def db():
    db = Database()
    return db

@pytest.fixture
def burger():
    burger = Burger()
    return burger

@pytest.fixture
def burger_with_ingredients_and_bun(burger, mocker):
    mock_bun = mocker.Mock()
    mock_bun.get_name.return_value = 'black bun'
    mock_bun.get_price.return_value = 100.0
    burger.bun = mock_bun

    mock_ingredient = mocker.Mock()
    mock_ingredient.get_price.return_value = 50.0
    mock_ingredient.get_name.return_value = 'hot sauce'
    mock_ingredient.get_type.return_value = ingredient_types.INGREDIENT_TYPE_SAUCE

    mock_ingredient2 = mocker.Mock()
    mock_ingredient2.get_price.return_value = 60.3
    mock_ingredient2.get_type.return_value = ingredient_types.INGREDIENT_TYPE_FILLING
    mock_ingredient2.get_name.return_value = 'cutlet'

    mock_ingredient3 = mocker.Mock()
    mock_ingredient3.get_price.return_value = 70.7
    mock_ingredient3.get_type.return_value = ingredient_types.INGREDIENT_TYPE_SAUCE
    mock_ingredient3.get_name.return_value = 'chili sauce'

    burger.ingredients = [mock_ingredient, mock_ingredient2, mock_ingredient3]
    return burger