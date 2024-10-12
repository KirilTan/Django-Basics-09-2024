from django.contrib import admin

from djangoProject1.departments.models import Department


# Register your models here.
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
    )

    search_fields = (
        'name',
        'slug',
    )

    list_filter = (
        'name',
    )
    