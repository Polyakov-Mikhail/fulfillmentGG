from django.contrib import admin
from ful.models import FAQ, CategoryFAQ, Services, Warehouses, JobTitle, Employees


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'answer')


@admin.register(CategoryFAQ)
class CategoryFAQAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price', 'measurement', 'image',)


@admin.register(Warehouses)
class WarehousesAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'address', 'slug', 'image',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(JobTitle)
class JobTitleAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name', 'job_title', 'warehouse', 'photo',)
