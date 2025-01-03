from django.db import models

NULLABLE = {"blank": True, "null": True}


class Start(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Стартовая позиция",
        help_text="Введите стартовые позиции")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Старт'
        verbose_name_plural = 'Старты'