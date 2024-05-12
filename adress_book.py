"""AddressBook"""

from collections import UserDict
from record import Record
from custom_exceptions import NameIsAlreadyInTheBook, NameIsNotFoundError


class AddressBook(UserDict):
    """AddressBook"""

    def is_name_in_address_book(self, name: str):
        """Check if name is in the adress Book"""
        return name in self.data

    def add_record(self, record: Record):
        """Add record to the address Book"""
        user_name = record.name.value

        if self.is_name_in_address_book(user_name):
            raise NameIsAlreadyInTheBook(user_name)

        self.data[user_name] = record

    def find(self, name: str):
        """Find user in an address Book by the name"""
        if not self.is_name_in_address_book(name):
            raise NameIsNotFoundError(name)

        return self.data[name]

    def delete(self, name: str):
        """Delete record by the name"""
        if not self.is_name_in_address_book(name):
            raise NameIsNotFoundError(name)

        del self.data[name]


if __name__ == "__main":
    pass
