from django.db import models
from django.utils.text import slugify
from unidecode import unidecode

NULLABLE = {"blank": True, "null": True}


class Start(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Стартовая позиция",
        help_text="Введите стартовые позиции",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Старт"
        verbose_name_plural = "Старты"


class CategoryFAQ(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Категория вопроса",
        help_text="Введите категорию вопроса",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория вопроса"
        verbose_name_plural = "Категории вопросов"


class FAQ(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Вопрос",
        help_text="Введите частый вопрос",
    )
    answer = models.TextField(
        verbose_name="Ответ на вопрос", help_text="Введите ответ на вопрос"
    )
    category = models.ForeignKey(
        CategoryFAQ,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="Введите категорию вопроса",
        **NULLABLE,
        related_name="faq"

    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"


class Services(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Услуга",
        help_text="Введите услугу",
    )
    description = models.TextField(
        verbose_name="Описание услуги", help_text="Введите описание услуги",
        **NULLABLE,
    )
    price = models.IntegerField(
        verbose_name="Стоимость услуги", help_text="Введите стоимость услуги"
    )
    measurement = models.CharField(
        max_length=100,
        verbose_name="Единица измерения",
        help_text="Введите единицу измерения",
        **NULLABLE,
    )
    image = models.ImageField(
        upload_to="services/image",
        verbose_name="Изображение услуги (превью)",
        **NULLABLE,
        help_text="Загрузите изображение услуги",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"


class Warehouses(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название склада",
        help_text="Введите название склада",
    )
    city = models.CharField(
        max_length=30,
        verbose_name="Город нахождения склада",
        help_text="Укажите город, где находится склад",
    )
    address = models.CharField(
        max_length=100,
        verbose_name="Адрес склада",
        help_text="Укажите адрес склада",
    )
    slug = models.SlugField(
        max_length=100,
        verbose_name="URL",
        help_text="Можно вручную исправить URL",
        **NULLABLE,
        unique=True,
    )
    image = models.ImageField(
        upload_to="warehouses/image",
        verbose_name="фотография склада",
        **NULLABLE,
        help_text="Загрузите фотографию склада",
    )

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(unidecode(self.name))
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Склад"
        verbose_name_plural = "Склады"
    

class JobTitle(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Должность",
        help_text="Введите должность",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"


class Employees(models.Model):
    last_name = models.CharField(
        max_length=30,
        verbose_name="Фамилия сотрудника",
        help_text="Введите фамилию сотрудника",
    )
    first_name = models.CharField(
        max_length=30,
        verbose_name="Имя сотрудника",
        help_text="Введите имя сотрудника",
    )
    job_title = models.ForeignKey(
        JobTitle,
        on_delete=models.SET_NULL,
        verbose_name="Должность сотрудника",
        help_text="На каком должности работает сотрудник?",
        **NULLABLE,
        related_name="job_title"
    )
    warehouse = models.ForeignKey(
        Warehouses,
        on_delete=models.SET_NULL,
        verbose_name="Склад",
        help_text="На каком складе работает сотрудник?",
        **NULLABLE,
        related_name="warehouse"
    )
    photo = models.ImageField(
        upload_to="employees/image",
        verbose_name="фотография сотрудника",
        **NULLABLE,
        help_text="Загрузите фотографию",
    )

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"



