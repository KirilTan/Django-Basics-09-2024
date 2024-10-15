from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class FileSizeValidator:
    def __init__(self, max_size_mb: int, error_message: str = None):
        self.max_size_mb = max_size_mb
        self.error_message = error_message

    @property
    def error_message(self):
        return self.__error_message

    @error_message.setter
    def error_message(self, value):
        if value is None:
            self.__error_message = f"File size should not exceed {self.max_size_mb}MB."

        self.__message = value

    def __call__(self, value):
        if value.size > (self.max_size_mb * 1024 * 1024):
            raise ValidationError(self.error_message)
