from django.contrib import admin

from djangoProject.todo_app.models import Task


# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    search_fields = (
        'name',
    )

    list_filter = (
        'created_at',
        'name',
    )

    list_display = (
        'id',
        'name',
        'description',
        'created_at'
    )

    fieldsets = \
        (
            (
                'Name and Description',
                {
                    'fields':
                        (
                            'name',
                            'description',
                        )
                }
            ),
        )
