"""A test source file for the unittest template generator."""


def my_global_method_01(param1: str, param2: int, param3) -> list[bool]:
    """Global method with parameters."""
    return []


class MyClass:
    """Class without inheritance."""
    def __init__(self):
        self.name = "MyClass"

    def my_class_method_01(self, param1: str, param2: int, param3) -> list[bool]:
        """Class method with parameters."""
        return []

    def my_class_method_02(self):
        """Class method without parameters."""
        return

    def _my_private_method(self):
        return


class MyClassWithInh(MyClass):
    """Class with inheritance."""
    def __init__(self):
        super().__init__()

    def my_class_method_02(self):
        """Class method without parameters."""
        return


def my_global_method_02():
    """Global method without parameters. Intentionally put at a weird space in the file."""
    return
