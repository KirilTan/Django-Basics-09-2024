import os
import django
from django.utils.text import slugify

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject1.settings')
django.setup()

# Import models
from djangoProject1.departments.models import Department

# Create queries withing functions
def create_departments(*args, **kwargs):
    departments = []

    # Handle department names from args (auto-generate slugs)
    for name in args:
        if name:  # Ensure name is not empty
            slug = slugify(name)
            departments.append(Department(name=name, slug=slug))

    # Handle department names and custom slugs from kwargs
    for name, slug in kwargs.items():
        if name:  # Ensure name is not empty
            slug = slug or slugify(name)  # Use the provided slug, or generate it if missing
            departments.append(Department(name=name, slug=slug))

    # Bulk create all departments
    Department.objects.bulk_create(departments)

def delete_all_departments():
    Department.objects.all().delete()

