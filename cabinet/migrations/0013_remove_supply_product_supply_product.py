# Generated by Django 4.2.2 on 2025-01-16 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cabinet", "0012_alter_supply_options"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="supply",
            name="product",
        ),
        migrations.AddField(
            model_name="supply",
            name="product",
            field=models.ManyToManyField(
                blank=True,
                help_text="товар личного кабинета",
                null=True,
                related_name="product_supply",
                to="cabinet.product",
                verbose_name="товар",
            ),
        ),
    ]
