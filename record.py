"""Record module"""

from name import Name
from phone import Phone
from custom_exceptions import PhoneIsAlreadyInTheListError, PhoneIsNotFoundError

class Record:
    """CRUD for Record"""
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def is_phone_in_the_list(self, phone: str) -> bool:
        """Check if phone number is already in the list"""
        phone_as_obj = Phone(phone)
        return phone_as_obj in self.phones

    def add_phone(self, phone: str) -> None:
        """Add phone if it is not exist"""

        """Check if phone is not present in the list"""
        if self.is_phone_in_the_list(phone):
            raise PhoneIsAlreadyInTheListError(phone)

        phone_as_obj = Phone(phone)
        self.phones.append(phone_as_obj)

    def edit_phone(self, old_phone: str, new_phone: str) -> None:
        """Edit number if it is already exist in the list"""

        """Check if old phone is present in the list"""
        if not self.is_phone_in_the_list(old_phone):
            raise PhoneIsNotFoundError(old_phone)

        """Check if new phone is not present in the list"""
        if self.is_phone_in_the_list(new_phone):
            raise PhoneIsAlreadyInTheListError(new_phone)

        old_phone_as_phone_obj = Phone(old_phone)
        self.phones[self.phones.index(old_phone_as_phone_obj)] = Phone(new_phone)

    def find_phone(self, phone: str):
        """Find phone in the list"""
        if not self.is_phone_in_the_list(phone):
            raise PhoneIsNotFoundError(phone)

        phone_as_obj = Phone(phone)
        return self.phones[self.phones.index(phone_as_obj)]

    def remove_phone(self, phone: str) -> None:
        """Remove phone from the list"""
        if not self.is_phone_in_the_list(phone):
            raise PhoneIsNotFoundError(phone)

        phone_as_obj = Phone(phone)
        del self.phones[self.phones.index(phone_as_obj)]

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


if __name__ == "__main":
    pass
