import pytest

from practicum.bun import Bun


class TestBun:

    @pytest.mark.parametrize('name', ['Булка', 'Вкусная булка', ''])
    def test_bun_init_correct_data_create_bun_with_correct_name(self, name):
        bun = Bun(name, 7.2)
        assert bun.name == name

    @pytest.mark.parametrize('price', [7.2, 7.0, 123.45])
    def test_bun_init_correct_data_create_bun_with_correct_price(self, price):
        bun = Bun('Булка', price)
        assert bun.price == price

    
    def test_get_name_return_correct_name(self, bun):
        assert bun.get_name() == 'Булка'


    def test_get_price_return_correct_price(self, bun):
        assert bun.get_price() == 7.2

    
