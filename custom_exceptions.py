"""Custom exception for Module 6"""


class PhoneIsNotFoundError(Exception):
    """Exception for record module"""
    def __init__(self, phone: str):
        message = f"Phone: {phone} is not found in the list"
        super().__init__(message)


class PhoneIsAlreadyInTheListError(Exception):
    """Exception for record module"""
    def __init__(self, phone: str):
        message = f"Phone: {phone} is already in the list"
        super().__init__(message)


class PhoneValidationError(Exception):
    """Exception for phone module"""
    def __init__(self, phone: str):
        message = f"Phone: {phone} must consist of 10 digits"
        super().__init__(message)


class NameIsNotFoundError(Exception):
    """Exception for address_book module"""
    def __init__(self, name: str):
        message = f"Name: {name} is not found in the address Book"
        super().__init__(message)


class NameIsAlreadyInTheBook(Exception):
    """Exception for address_book module"""
    def __init__(self, name: str):
        message = f"Name: {name} is already in the address Book"
        super().__init__(message)


if __name__ == "__main":
    pass
