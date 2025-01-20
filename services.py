from django.core.cache import cache
from config.settings import CACHE_ENABLED
from django.conf import settings


def get_models_from_cache(model):
    """
    Получает продукт из кэша, если кэш пустой, получает данные из БД
    """

    if not CACHE_ENABLED:
        return model.objects.all()

    # Получение имени модели из имени класса
    name_model = model.__name__.lower()
    # Получение ключа для кэширования для моделей для общего списка ("модель_list")
    key = f"{name_model}_list"

    models_cache = cache.get(key)

    # Если кэш не пустой, возвращаем данные из кэша
    if models_cache is not None:
        return models_cache

    # Если кэш пустой, получаем данные из БД и добавляем их в кэш
    models_cache = model.objects.all()
    cache.set(key, models_cache)
    return models_cache
