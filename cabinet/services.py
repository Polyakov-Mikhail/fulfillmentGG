# def get_product_count():
#     if settings.CACHE_ENABLED:
#         key = 'mailing_quantity'
#         mailing_quantity = cache.get(key)
#         if mailing_quantity is None:
#             mailing_quantity = Mailing.objects.all().count()
#             cache.set(key, mailing_quantity)
#     else:
#         mailing_quantity = Mailing.objects.all().count()
#
#     return mailing_quantity