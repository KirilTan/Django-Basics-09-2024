from django.shortcuts import render

# Create your views here.
def photo_edit_page(request, pk: int):
    return render(request, 'photos/photo-edit-page.html')

def photo_details_page(request, pk:int):
    return render(request, 'photos/photo-details-page.html')

def photo_add_page(request):
    return render(request, 'photos/photo-add-page.html')
