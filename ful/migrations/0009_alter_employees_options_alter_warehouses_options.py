# Generated by Django 4.2.2 on 2025-01-07 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("ful", "0008_jobtitle_warehouses_employees"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="employees",
            options={"verbose_name": "Сотрудник", "verbose_name_plural": "Сотрудники"},
        ),
        migrations.AlterModelOptions(
            name="warehouses",
            options={"verbose_name": "Склад", "verbose_name_plural": "Склады"},
        ),
    ]
