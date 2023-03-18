# корзина будет храниться в сессии в виде пар "ключ-значение"
# в качестве ключа будет использоваться id товара, а в качестве значения - кол-во
# данного товара

class Cart:
    def __init__(self, request):
        self.session = request.session  # сохраняем ссылку на сессию в переменной self.session
        if 'cart' not in self.session.keys():  # проверяем есть ли корзина у пользователя
            self.session['cart'] = dict()  # создаём новый словарь в качестве корзины

    def add(self, prod_id, prod_count):
        if prod_id in self.session['cart'].keys():
            raise AttributeError(f'Товар с id {prod_id} уже есть в корзине!')
        self.session['cart'][prod_id] = prod_count

    # +=
    def __iadd__(self, kv_pair):  # key-value
        self.add(*kv_pair)
        #self.add(kv_pair[0], kv_pair[1])

    def change(self, prod_id, prod_count):  # изменить
        try:  # если get генерирует исключение, то переходим к блоку except
            self.get(prod_id)
            self.session['cart'][prod_id] = prod_count
        except AttributeError as e:  # "пробрасываем" исключение вверх по стеку
            raise e

    # cart[key] = value
    def __setitem__(self, key, value):
        try:  # добавляем товар в корзину
            self.add(key, value)
        except AttributeError:  # если он уже есть в корзине, изменяем его кол-во
            self.change(key, value)

    # cart[key]
    def __getitem__(self, key):
        return self.get(key)

    def get(self, key):  # get - получить кол-во товара
        if key not in self.session['cart']:  # если товара с id key нет в корзине
            raise AttributeError(f'Товара с id {key} нет в корзине!')  # генерируем исключение
        return self.session['cart'][key]  # возвращаем кол-во товара с id key в корзине

    def del_(self, key):  # удаление товара из корзины
        del self.session['cart'][key]

    def __delitem__(self, key):  # del cart[4]
        self.del_(key)

    def __iter__(self):  # для перебора корзины в циклах (она является словарём)
        for key, value in self.session['cart'].items():
            yield (key, value)  # порождаем пары ключ-значение

