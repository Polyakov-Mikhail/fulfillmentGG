from django.db import models
from datetime import datetime

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

    class Meta:
        verbose_name = "Владелец кабинета"
        verbose_name_plural = "Владельцы кабинетов"

    def __str__(self):
        return self.name


class Supply(models.Model):
    class StatusSupply(models.TextChoices):
        CREATED = 'Создана', 'Создана'
        WAY = 'В пути', 'В пути'
        ACCEPTANCE = 'Приемка', 'Приемка'
        ACCEPTED = 'Принята', 'Принята'

    delivery_date = models.DateField(
        verbose_name="Дата поступления товара",
        help_text="Укажите дату, когда приедет товар",
    )
    owner = models.ForeignKey(
        User,
        verbose_name="Владелец",
        help_text="Укажите владельца поставки",
        **NULLABLE,
        on_delete=models.SET_NULL
    )
    quantity_cargo = models.PositiveIntegerField(
        verbose_name="количество грузовых мест",
        help_text="Укажите количество грузовых мест в поставке",
        default=0,
    )
    status = models.CharField(
        max_length=10,
        verbose_name="Статус перевозки",
        choices=StatusSupply.choices,
        default = StatusSupply.CREATED
    )

    class Meta:
        verbose_name = "Поставка"
        verbose_name_plural = "Поставки"

    def __str__(self):
        return f'{self.status} от {self.delivery_date.strftime('%Y-%m-%d')}. Владелец {self.owner}'


class ProductAccept(models.Model):
    owner = models.ForeignKey(
        User,
        **NULLABLE,
        verbose_name="Владелец",
        help_text="Укажите владельца товара",
        on_delete=models.SET_NULL
    )
    product = models.ForeignKey(
        Product,
        **NULLABLE,
        verbose_name="товар",
        help_text="Добавьте товар",
        related_name="product_supply",
        on_delete=models.SET_NULL
    )
    quantity = models.PositiveIntegerField(
        verbose_name="количество товара",
        help_text="Укажите количество товара, который приедет",
    )
    supply = models.ForeignKey(
        Supply,
        **NULLABLE,
        verbose_name="Поставка",
        help_text="Укажите в какой поставке приедет",
        on_delete=models.SET_NULL,
        related_name="supply",
    )

    class Meta:
        verbose_name = "Поступление товаров"
        verbose_name_plural = "Поступления товаров"

    def __str__(self):
        return f'{self.product} владелец {self.owner}'


class Marketplace(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название маркетплейса",
        help_text="Введите название макретплейса",
    )

    class Meta:
        verbose_name = "Маркетплейс"
        verbose_name_plural = "Маркетплейсы"

    def __str__(self):
        return self.name


class DeliveryPoint(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название точки доставки",
        help_text="Введите название точки доставки",
    )
    city = models.CharField(
        max_length=30,
        verbose_name="Город нахождения точки доставки",
        help_text="Укажите город доставки",
    )
    address = models.CharField(
        max_length=100,
        verbose_name="Адрес точки доставки",
        help_text="Укажите адрес доставки",
    )
    marketplace = models.ForeignKey(
        Marketplace,
        verbose_name="Маркетплейс",
        help_text="Укажите маркетплейс",
        on_delete=models.CASCADE,
        related_name="marketplace",
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Активный',
    )

    class Meta:
        verbose_name = "Адрес доставки"
        verbose_name_plural = "Адреса доставки"

    def __str__(self):
        return self.name


class Shipment(models.Model):
    class StatusShipment(models.TextChoices):
        CREATED = 'Создана', 'Создана'
        WAY = 'Отправлена', 'Отправлена'
        DELIVERED = 'Доставлена', 'Доставлена'

    shipment_date = models.DateField(
        verbose_name="Дата отгрузки товара",
        help_text="Укажите дату отгрузки товар",
    )
    owner = models.ForeignKey(
        User,
        verbose_name="Владелец",
        help_text="Укажите владельца поставки",
        **NULLABLE,
        on_delete=models.SET_NULL
    )
    delivery_point = models.ForeignKey(
        DeliveryPoint,
        on_delete=models.PROTECT,
        verbose_name="Точка доставки",
        help_text="Укажите куда доставить товар",
        related_name="delivery_point",
    )
    quantity_cargo = models.PositiveIntegerField(
        verbose_name="количество грузовых мест",
        help_text="Укажите количество грузовых мест в поставке",
        default=0,
    )
    status = models.CharField(
        max_length=10,
        verbose_name="Статус отгрузки",
        choices=StatusShipment.choices,
        default = StatusShipment.CREATED
    )
    comment = models.TextField(
        verbose_name="Комментарий",
        help_text="Укажите комментарий, либо адрес доставки, если нет в списке",
        **NULLABLE,
    )

    class Meta:
        verbose_name = "Отгрузка"
        verbose_name_plural = "Отгрузки"

    def __str__(self):
        return f'Поставка в {self.delivery_point} {self.status} от {self.shipment_date.strftime('%Y-%m-%d')}. Владелец {self.owner}'


class ProductShipment(models.Model):
    owner = models.ForeignKey(
        User,
        **NULLABLE,
        verbose_name="Владелец",
        help_text="Укажите владельца товара",
        on_delete=models.SET_NULL
    )
    product = models.ForeignKey(
        Product,
        **NULLABLE,
        verbose_name="товар",
        help_text="Добавьте товар",
        related_name="product_shipment",
        on_delete=models.SET_NULL
    )
    quantity = models.PositiveIntegerField(
        verbose_name="количество товара",
        help_text="Укажите количество товара, который приедет",
    )
    shipment = models.ForeignKey(
        Shipment,
        **NULLABLE,
        verbose_name="Отгрузка",
        help_text="Укажите в какой отгрузке уедет",
        on_delete=models.SET_NULL,
        related_name="shipment",
    )

    class Meta:
        verbose_name = "Отгрузка товара"
        verbose_name_plural = "Отгрузки товаров"

    def __str__(self):
        return f'{self.product} владелец {self.owner}'