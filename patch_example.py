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
    

@patch('__main__.Class.method')
@patch('__main__.Class.method_two')
def my_function(mock_method_two, mock_method):
    mock_method.return_value = 'foo'
    mock_method_two.side_effect = KeyError('key error exceptoin') # Throw exception when method is called.
    

mock_class = MagicMock()
mock_class.method_one.return_value = 1
mock_class.method_two.side_effect = KeyError('key error exceptoin') # Throw exception when method is called.


