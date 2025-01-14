# Generated by Django 4.2.2 on 2025-01-03 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Start",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        help_text="Введите стартовые позиции",
                        max_length=100,
                        verbose_name="Стартовая позиция",
                    ),
                ),
            ],
            options={
                "verbose_name": "Старт",
                "verbose_name_plural": "Старты",
            },
        ),
    ]
