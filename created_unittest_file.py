"""Unittest for the file test_source_file.py."""

import unittest


class TestGlobalMethods(unittest.TestCase):
    """Test case for all global methods."""
    def todo_test_my_global_method_01(self):
        """Test the method my_global_method_01(param1: str, param2: int, param3) -> list[bool]"""
        self.fail()

    def todo_test_my_global_method_02(self):
        """Test the method my_global_method_02()"""
        self.fail()


class TestMyClass(unittest.TestCase):
    """Test case for all methods of the class MyClass."""
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def todo_test_init(self):
        """Test the method __init__(self)"""
        self.fail()

    def todo_test_my_class_method_01(self):
        """Test the method my_class_method_01(self, param1: str, param2: int, param3) -> list[bool]"""
        self.fail()

    def todo_test_my_class_method_02(self):
        """Test the method my_class_method_02(self)"""
        self.fail()

    def todo_test_my_private_method(self):
        """Test the method _my_private_method(self)"""
        self.fail()


class TestMyClassWithInh(unittest.TestCase):
    """Test case for all methods of the class MyClassWithInh(MyClass)."""
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def todo_test_init(self):
        """Test the method __init__(self)"""
        self.fail()

    def todo_test_my_class_method_02(self):
        """Test the method my_class_method_02(self)"""
        self.fail()

