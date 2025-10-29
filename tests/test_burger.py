import pytest


class TestBurger:

    def test_burger_init_bun_is_none(self, burger):
        assert burger.bun is None


    def test_burger_init_ingre_is_empty_list(self, burger):
        assert burger.ingredients == []


    def test_set_buns_correct_bun_add_bun_in_burger(self, burger, mocker):
        mock_bun = mocker.Mock()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun


    def test_add_ingredient_correct_ingredient_add_ingredient_in_burger(self, burger, mocker):
        mock_ingredient = mocker.Mock()
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients[0] == mock_ingredient     


    def test_add_ingredient_correct_ingredients_add_ingredients_in_burger(self, burger_with_ingredients_and_bun, mocker):
        assert len(burger_with_ingredients_and_bun.ingredients) == 3     


    def test_remove_ingredient_correct_index_delete_ingredient(self, burger_with_ingredients_and_bun):
        burger_with_ingredients_and_bun.remove_ingredient(0)
        assert len(burger_with_ingredients_and_bun.ingredients) == 2


    def test_remove_ingredient_correct_index_delete_ingredient_with_index(self, burger, mocker):
        mock_ingredient = mocker.Mock()
        mock_ingredient2 = mocker.Mock()
        mock_ingredient3 = mocker.Mock()
        burger.ingredients = [mock_ingredient, mock_ingredient2, mock_ingredient3]
        burger.remove_ingredient(0)
        assert burger.ingredients == [mock_ingredient2, mock_ingredient3]


    def test_move_ingredient_index0_index1_move_element0_to_place_element1(self, burger, mocker):
        mock_ingredient = mocker.Mock()
        mock_ingredient2 = mocker.Mock()
        mock_ingredient3 = mocker.Mock()
        burger.ingredients = [mock_ingredient, mock_ingredient2, mock_ingredient3]
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [mock_ingredient2, mock_ingredient, mock_ingredient3]


    def test_get_price_correct_burger_return_correct_price(self, burger_with_ingredients_and_bun):
        assert burger_with_ingredients_and_bun.get_price() == 381

    @pytest.mark.parametrize('number_line', [0, 4])
    def test_get_receipt_correct_burger_contain_name_bun_first_and_fifth_line(self, burger_with_ingredients_and_bun, number_line):
        first_line = burger_with_ingredients_and_bun.get_receipt().split('\n')[number_line]
        assert f'(==== {burger_with_ingredients_and_bun.bun.get_name()} ====)' in first_line
    
    @pytest.mark.parametrize('number_line, index', [(1, 0), (2, 1), (3, 2)])
    def test_get_receipt_correct_burger_contain_type_and_name_ingredient_in_correct_line(self, burger_with_ingredients_and_bun, number_line, index):
        line = burger_with_ingredients_and_bun.get_receipt().split('\n')[number_line]
        assert f'= {str(burger_with_ingredients_and_bun.ingredients[index].get_type()).lower()} {burger_with_ingredients_and_bun.ingredients[index].get_name()} =' \
        in line

    def test_get_receipt_correct_burger_contain_correct_price_in_last_line(self, burger_with_ingredients_and_bun):
        last_line = burger_with_ingredients_and_bun.get_receipt().split('\n')[-1]
        assert f'Price: {burger_with_ingredients_and_bun.get_price()}' in last_line

