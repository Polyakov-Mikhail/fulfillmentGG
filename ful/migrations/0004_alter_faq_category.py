# Generated by Django 4.2.2 on 2025-01-05 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("ful", "0003_categoryfaq_faq_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="faq",
            name="category",
            field=models.ForeignKey(
                blank=True,
                help_text="Введите категорию вопроса",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="category",
                to="ful.categoryfaq",
                verbose_name="Категория",
            ),
        ),
    ]
