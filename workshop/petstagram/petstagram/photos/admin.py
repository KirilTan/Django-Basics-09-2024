from django.contrib import admin

from petstagram.photos.models import Photo


# Register your models here.
@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'description',
        'date_of_publication',
        'location',
    )

    list_filter = (
        'date_of_publication',
        'location',
        'description',
    )

    search_fields = (
        'description',
        'location',
    )