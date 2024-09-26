# Generated by Django 4.2.16 on 2024-09-20 18:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                default=datetime.datetime(2024, 9, 20, 21, 6, 42, 870601),
                help_text="Укажите дату создания",
                verbose_name="Дата создания",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.PositiveIntegerField(
                help_text="Введите цену за покупку", verbose_name="Цена за покупку"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="updated_at",
            field=models.DateTimeField(
                auto_now=True,
                default=datetime.datetime(2024, 9, 20, 21, 6, 56, 376295),
                help_text="Укажите дату последнего изменения",
                verbose_name="Дата последнего изменения",
            ),
            preserve_default=False,
        ),
    ]