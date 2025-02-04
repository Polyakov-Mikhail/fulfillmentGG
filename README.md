### Описание задачи:

Необходимо создать сайт для компании-фулфилмента для селлеров. Сайт должен быть сверстан и подключен к админке. Для выполнения задачи необходимо использовать Django. Сайт должен содержать основные разделы, необходимые для функционирования компании-фулфилмента.

 

### Задача

1. Сверстать сайт для компании-фулфилмента.
2. Подключить сайт к админке Django.
3. Создать адаптивный и привлекательный интерфейс.

 

### Функционал сайта:

1. **Главная страница**: 
   - Описание компании.
   - Перечень предоставляемых услуг.
   - Контактная информация.
   - Форма для обратной связи.
2. **Страница "О компании"**: 
   - История компании.
   - Миссия и ценности.
   - Команда компании.
3. **Страница услуг**: 
   - Перечень предоставляемых услуг.
   - Подробное описание каждой услуги.
   - Цены на услуги.
4. **Страница "Контакты"**: 
   - Адрес компании.
   - Карта проезда.
   - Контактные телефоны и email.
   - Форма обратной связи.
5. **Личный кабинет**: 
   - Регистрация и авторизация пользователей.
   - Возможность внесения информации по своему товару.
   - Формирование информации о поступлении товара на склад фулфилмента.
   - Просмотр товарного остатка.
   - Формирование задания на отгрузку.
6. **Админка**: 
   - Управление пользователями.
   - Управление услугами.
   - Управление товарами.
 

### Технические требования:

1. **Фреймворк**: 
   - Использовать фреймворк Django для реализации проекта.
2. **База данных**: 
   - Использовать PostgreSQL для хранения данных.
3. **Фронтенд**: 
   - Использовать Bootstrap или другой фреймворк для создания адаптивного интерфейса.
4. **Контейнеризация**: 
   - Использовать Docker и Docker compose для контейнеризации приложения.
5. **Документация**: 
   - В корне проекта должен быть файл README.md с описанием структуры проекта и инструкциями по установке и запуску.
6. **Качество кода**: 
   - Соблюдать стандарты PEP8.
   - Весь код должен храниться в удаленном Git репозитории.

## Использование

Для использования программы необходимо установить `poetry` и выполнить следующие шаги:

1. Клонирование репозитория
```bash
git@github.com:Polyakov-Mikhail/fulfillmentGG.git
или
https://github.com/Polyakov-Mikhail/fulfillmentGG.git
```
2. Установление зависимостей
```bash
poetry shell
poetry install
```
3. Создание файла .env: 
```text
Вставить свои значения в переменные из файла .env.sample
```
4. Установка базы данных
```text
python3 manage.py loaddata data.json
```
5. Запуск проекта
```text
python3 manage.py runserver
```
