import os
import django

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject1.settings')
django.setup()

# Import models
from djangoProject1.departments.models import Department

# Create queries withing functions
def create_departments(**kwargs):
    departments = [Department(name=name, slug=slug) for name, slug in kwargs.items()  if name and slug]
    Department.objects.bulk_create(departments)

# create_departments(finance="finance", hr="human-resources", marketing="marketing")
