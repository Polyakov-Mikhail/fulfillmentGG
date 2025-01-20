# Generated by Django 4.2.2 on 2025-01-20 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cabinet", "0024_company_owner"),
    ]

    operations = [
        migrations.AlterField(
            model_name="company",
            name="current_account",
            field=models.TextField(
                help_text="Укажите расчетный счет компании",
                verbose_name="Расчетный счет компании",
            ),
        ),
        migrations.AlterField(
            model_name="company",
            name="inn",
            field=models.TextField(
                help_text="Укажите ИНН компании", verbose_name="ИНН компании"
            ),
        ),
    ]
