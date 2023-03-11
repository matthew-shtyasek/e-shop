from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=124, verbose_name='Название категории')

    class Meta:
        ordering = ('category_name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категорий'

    def __str__(self):
        return self.category_name


class Country(models.Model):
    country_name = models.CharField(max_length=32)

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

    def __str__(self):
        return self. country_name

class Manufacturer(models.Model):
    manufacturer_name = models.CharField(max_length=32, verbose_name='Название производителя')
    address = models.CharField(max_length=124, verbose_name='Адрес производителя')
    phone = models.PositiveIntegerField(verbose_name='Номер телефона')
    country_name = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name='Страна')

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'

    def __str__(self):
        return self.manufacturer_name


class Product(models.Model):
    product_name = models.CharField(max_length=64, verbose_name='Название продукта')
    manufacturer_name = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, verbose_name='Название производителя')
    guaranty = models.PositiveIntegerField(verbose_name='Гарантия')
    count = models.PositiveIntegerField(verbose_name='Количество')
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Название категории')

    class Meta:
        ordering = ('product_name',)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.product_name