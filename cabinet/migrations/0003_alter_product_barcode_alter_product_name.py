# Generated by Django 4.2.2 on 2025-01-11 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cabinet", "0002_alter_product_is_active"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="barcode",
            field=models.PositiveIntegerField(
                blank=True,
                help_text="Введите штрихкод товара",
                null=True,
                unique=True,
                verbose_name="штрихкод",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="name",
            field=models.CharField(
                help_text="Введите наименование товара",
                max_length=100,
                unique=True,
                verbose_name="Наименование",
            ),
        ),
    ]
