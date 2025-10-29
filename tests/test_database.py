import pytest

from practicum.database import Database
from practicum import ingredient_types


class TestDatabase:

    def test_database_init_contains_list_buns(self, db):
        assert type(db.buns) is list

    
    def test_database_init_contains_list_ingredients(self, db):
        assert type(db.ingredients) is list


    @pytest.mark.parametrize('name, price', [("black bun", 100), 
                                             ("white bun", 200),
                                             ("red bun", 300)])
    def test_database_init_list_buns_contains_bun(self, name, price, mocker):

        mock_bun_class = mocker.patch("practicum.database.Bun")
        mock_bun = mocker.Mock()
        mock_bun.name = name
        mock_bun.price = price
        mock_bun_class.return_value = mock_bun
        db = Database()
        for bun in db.buns:
            bun_in_list = False
            if bun.name == name and bun.price == price:
                bun_in_list = True
                break

        assert bun_in_list is True


    @pytest.mark.parametrize('type, name, price', [(ingredient_types.INGREDIENT_TYPE_SAUCE, "hot sauce", 100), 
                                             (ingredient_types.INGREDIENT_TYPE_SAUCE, "sour cream", 200),
                                             (ingredient_types.INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
                                             (ingredient_types.INGREDIENT_TYPE_FILLING, "cutlet", 100),
                                             (ingredient_types.INGREDIENT_TYPE_FILLING, "dinosaur", 200),
                                             (ingredient_types.INGREDIENT_TYPE_FILLING, "sausage", 300)]
                                             )
    def test_database_init_list_ingredients_contains_ingredient(self, type, name, price, mocker):
        
        mock_ingredient_class = mocker.patch("practicum.database.Ingredient")
        mock_ingredient = mocker.Mock()
        mock_ingredient.type = type
        mock_ingredient.name = name
        mock_ingredient.price = price
        mock_ingredient_class.return_value = mock_ingredient
        db = Database()
        for ingredient in db.ingredients:
           ingredient_in_list = False
           if ingredient.type == type and ingredient.name == name and ingredient.price == price:
                ingredient_in_list = True
                break
           
        assert ingredient_in_list is True


    def test_available_buns_return_list(self, db):
        assert type(db.available_buns()) is list

    def test_available_buns_return_list_with_buns(self, mocker):
        mock_bun_class = mocker.patch("practicum.database.Bun")
        mock_bun = mocker.Mock()
        mock_bun.name = "black bun"
        mock_bun.price = 100
        mock_bun_class.return_value = mock_bun
        db = Database()

        assert db.available_buns()[0] == mock_bun and len(db.available_buns()) == 3

        
    def test_available_ingredients_return_list(self, db):
        assert type(db.available_ingredients()) is list

    def test_available_ingredients_return_list_with_ingredients(self, mocker):
        mock_ingredient_class = mocker.patch("practicum.database.Ingredient")
        mock_ingredient = mocker.Mock()
        mock_ingredient.type = ingredient_types.INGREDIENT_TYPE_SAUCE
        mock_ingredient.name = "hot sauce"
        mock_ingredient.price = 100
        mock_ingredient_class.return_value = mock_ingredient
        db = Database()
        
        assert db.available_ingredients()[0] == mock_ingredient and len(db.available_ingredients()) == 6