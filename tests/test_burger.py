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

    
    def test_get_receipt_correct_burger_return_correct_receipt(self, burger_with_ingredients_and_bun):
        
        assert burger_with_ingredients_and_bun.get_receipt() == (
        '(==== black bun ====)\n'
        '= sauce hot sauce =\n'
        '= filling cutlet =\n'
        '= sauce chili sauce =\n'
        '(==== black bun ====)\n\n'
        'Price: 381.0')
    

