## Задание 1: Юнит-тесты

### Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers

### Реализованные сценарии

Созданы юнит-тесты, покрывающие классы `Bun`, `Burger`, `Ingredient`, `Database`

Процент покрытия 78% (отчет: `htmlcov/index.html`), так как `practikum.py` y не покрывался тестами

### Структура проекта

- `praktikum` - пакет, содержащий код программы
    `bun.py`
    `burger.py`
    `database.py`
    `ingredient_types.py`
    `ingredient.py`
    `practikum.py`
- `tests` - пакет, содержащий тесты, разделенные по классам:
    `test_bun.py`, 
    `test_burger.py`,
    `test_database.py`,
    `test_ingredient.py`

### Запуск автотестов

`$ pytest -v`

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Запуск автотестов и создание HTML-отчета о покрытии**

>  `$ pytest --cov=prakticum --cov-report=html`
