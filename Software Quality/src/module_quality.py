def simplest_func(a, b):
    assert isinstance(a, (int, float)), 'First argument is not int or float'
    assert isinstance(b, (int, float)), 'Second argument is not int or float'
    return a + b

