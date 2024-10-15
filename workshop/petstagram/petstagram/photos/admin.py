from django.contrib import admin

from petstagram.photos.models import Photo


# Register your models here.
@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'date_of_publication',
        'description',
        'location',
        'get_tagged_pets',
    )

    @staticmethod
    def get_tagged_pets(obj):
        return ', '.join(str(pet) for pet in obj.tagged_pets.all())

    list_filter = (
        'date_of_publication',
        'location',
        'description',
    )

    search_fields = (
        'description',
        'location',
    )