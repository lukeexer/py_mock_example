from unittest.mock import patch

class Class:
    def method(self):
        pass

with patch('__main__.Class') as MockClass:
    instance = MockClass()
    instance.method.return_value = 'foo'

    print(Class() is instance)
    print(instance.method())
    print(instance.method())
    print(instance.method.call_count)

    print(instance.method('a')) # Modify the argument 'a' as 'b' for testing the assertion.
    instance.method.assert_called_with('a'), '''the instance.method hasn't been called with 'a'.'''

with patch('__main__.Class.method') as mock_method:

    mock_method.return_value = 'foo'
