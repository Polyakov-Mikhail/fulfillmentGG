from django.db import models
from parso.python.tree import Class

from users.models import User

NULLABLE = {"blank": True, "null": True}


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование",
        help_text="Введите наименование товара",
        unique=True
    )
    article = models.CharField(
        max_length=20,
        verbose_name="артикул",
        help_text="Введите артикул товара",
        **NULLABLE,
    )
    barcode = models.PositiveIntegerField(
        verbose_name="штрихкод",
        help_text="Введите штрихкод товара",
        **NULLABLE,
        unique=True
    )
    quantity = models.PositiveIntegerField(
        verbose_name="количество товара",
        default=0,
        # editable=False,
    )
    image = models.ImageField(
        upload_to="product/image",
        verbose_name="Изображение(превью)",
        **NULLABLE,
        help_text="Загрузите изображение продукта",
    )
    owner = models.ForeignKey(
        User,
        verbose_name="Владелец",
        help_text="Укажите владельца товара",
        **NULLABLE,
        on_delete=models.SET_NULL

    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Активный',
    )
    description = models.TextField(
        verbose_name="Описание",
        help_text="Введите описание продукта",
        **NULLABLE,
    )
    created_at = models.DateField(
        verbose_name="Дата создания(записи в БД)",
        **NULLABLE,
        help_text="Укажите дату создания",
    )
    updated_at = models.DateField(
        verbose_name="Дата последнего изменения(записи в БД)",
        **NULLABLE,
        help_text="Укажите дату изменения",
    )

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


    def __str__(self):
        return self.name

class Dashboard(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование",
        help_text="Введите наименование дашборда",
        **NULLABLE,
        unique=True
    )
    owner = models.ForeignKey(
        User,
        verbose_name="Владелец",
        help_text="Укажите владельца личного кабинета",
        **NULLABLE,
        on_delete=models.SET_NULL
    )
    product = models.ForeignKey(
        Product,
        verbose_name="товар",
        help_text="товар личного кабинета",
        **NULLABLE,
        on_delete=models.SET_NULL,
        related_name="product",
    )

    class Meta:
        verbose_name = "Владелец кабинета"
        verbose_name_plural = "Владельцы кабинетов"

    def __str__(self):
        return self.name


class Supply(models.Model):
    class StatusSupply(models.TextChoices):
        CREATED = 'CD', 'Создана'
        ACCEPTANCE = 'AE', 'Приемка'
        ACCEPTED = 'FD', 'Принята'

    delivery_date = models.DateField(
        verbose_name="Дата поступления товара",
        help_text="Укажите дату, когда приедет товар",
    )
    owner = models.ForeignKey(
        User,
        verbose_name="Владелец",
        help_text="Укажите владельца личного кабинета",
        **NULLABLE,
        on_delete=models.SET_NULL
    )
    product = models.ManyToManyField(
        Product,
        verbose_name="товар",
        help_text="товар личного кабинета",
        **NULLABLE,
        related_name="product_supply",
    )
    quantity = models.PositiveIntegerField(
        verbose_name="количество товара",
        help_text="Укажите количество товара, который приедет",
    )
    status = models.CharField(
        max_length=2,
        verbose_name="Статус перевозки",
        choices=StatusSupply.choices,
        default = StatusSupply.CREATED
    )

    class Meta:
        verbose_name = "Поставка"
        verbose_name_plural = "Поставки"

    def __str__(self):
        return self.delivery_date
