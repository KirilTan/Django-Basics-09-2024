import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoProject.settings")
django.setup()

# Import your models
from djangoProject.todo_app.models import Task

# Create queries withing function
def create_tasks(name: str, description: str) -> str:
    """
    This function creates a new task in the Django application's database.

    Parameters:
        name (str): The name of the task.
        description (str): The description of the task.

    Returns:
        str: A success message indicating that the task has been created.
    """
    task = Task.objects.create(
        name=name,
        description=description
    )
    return f"'{name}' - '{description}' \n created successfully"


# create_tasks("Task 1", "This is task 1")
# create_tasks("Task 2", "This is task 2")
# create_tasks("Task 3", "This is task 3")
