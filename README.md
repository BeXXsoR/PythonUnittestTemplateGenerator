## Python unittest template generator ##
The python unittest template generator creates a template file for the unittest of any given python file using the unittest package. It supports the following features:

# Features #
- **Support classes and global methods**: For each class in the file, a new test class is created as a subclass of unittest.TestCase. For every method within this class, an individual test method is added. If there are any global methods in the python file, an extra class TestGlobalMethods is added, containing a test method for each global method.
- **Intuitive naming convention**: All test case classes are named "Test{OriginalClassName}". All methods are named "todo_test_{original_method_name}", with leading and trailing underscores being trimmed. Using the prefix "todo_" leads to the test method being ignored by the unittest framework, which enables the user to only activate the tests that are already implemented.
- **Docstring support**: Each test class and method gets a docstring that holds information about the original class or method (for example the method's syntax).
- **PEP 8 support**: The created file is compatible with the styleguide defined in PEP 8.

# Usage #
Start the generator with
````
python unittest_gen.py src_file trg_file [-ts tab_size]
````
where
- *src_file* is the path to the source python file, 
- *trg_file* is the destination for the unittest template file that will be created, and
- *tab_size* is the number of spaces to be used for a tab in the target file (default = 4). If 0 is set here, the tab character will be used.

# Examples #
The file *test_source_file.py* contains a sample python file to showcase the unittest template generator. The file *created_unittest_file.py* shows the result of the generator when executed as
````
python unittest_gen.py test_source_file.py created_unittest_file.py
````
