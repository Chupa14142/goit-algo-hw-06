"""Phone module"""

from field import Field
from custom_exceptions import PhoneValidationError


class Phone(Field):
    """Phone class"""

    def __init__(self, phone: str):
        Phone.validate_phone_number(phone)
        super().__init__(phone)

    def __eq__(self, other):
        return self.value == other.value

    @staticmethod
    def validate_phone_number(phone: str):
        """Validate one phone number - 10 digits"""
        if len(phone) != 10 or not phone.isdigit():
            raise PhoneValidationError(phone)


if __name__ == "__main":
    pass
