# Generated by Django 2.2 on 2023-03-11 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=124, verbose_name='Название категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категорий',
                'ordering': ('category_name',),
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(max_length=32)),
            ],
            options={
                'verbose_name': 'Страна',
                'verbose_name_plural': 'Страны',
            },
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer_name', models.CharField(max_length=32, verbose_name='Название производителя')),
                ('address', models.CharField(max_length=124, verbose_name='Адрес производителя')),
                ('phone', models.PositiveIntegerField(verbose_name='Номер телефона')),
                ('country_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Country', verbose_name='Страна')),
            ],
            options={
                'verbose_name': 'Производитель',
                'verbose_name_plural': 'Производителей',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=64, verbose_name='Название продукта')),
                ('guaranty', models.PositiveIntegerField(verbose_name='Гарантия')),
                ('count', models.PositiveIntegerField(verbose_name='Количество')),
                ('category_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Category', verbose_name='Название категории')),
                ('manufacturer_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Manufacturer', verbose_name='Название производителя')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'ordering': ('product_name',),
            },
        ),
    ]
