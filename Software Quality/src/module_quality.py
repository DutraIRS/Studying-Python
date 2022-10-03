"""This is the main module.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam risus tortor, molestie et dolor faucibus, rutrum ornare ligula. Nullam faucibus, augue in lobortis iaculis, ex lacus dictum felis, vel lacinia eros leo non urna. Nunc consectetur velit vitae dolor sodales, nec posuere elit convallis. Suspendisse porta lacus non sapien venenatis tempor. Donec nec diam non arcu tempor vestibulum. Integer sit amet nulla id mi lobortis maximus imperdiet ac leo. Maecenas ex mauris, efficitur vitae ligula sed, porttitor ornare magna. Donec ullamcorper, nibh in dictum commodo, leo ante blandit lacus, sed vestibulum sem dui id lacus. Nulla suscipit, nisi id venenatis scelerisque, ante sapien tempus odio, molestie tincidunt odio odio non mauris. Curabitur dignissim, arcu id euismod posuere, tellus tellus pretium est, vehicula feugiat tellus est nec enim. Nulla rhoncus ante sit amet sapien aliquet, vitae sagittis ex porttitor.
Interdum et malesuada fames ac ante ipsum primis in faucibus. In iaculis consequat ligula. Vestibulum eu commodo turpis. Nullam et rhoncus elit. Praesent sodales porttitor dictum. Donec semper, odio vel condimentum ultrices, dui enim ornare mi, sed tincidunt mi eros et sapien. Curabitur aliquam, ante eget tincidunt iaculis, nisl neque pharetra purus, a volutpat mauris nibh non nisi. Maecenas ex odio, imperdiet non condimentum ac, efficitur id ligula. Vivamus eu nibh et dolor interdum rhoncus a ut neque. Nullam quam erat, placerat sit amet sem ac, venenatis suscipit nisi. Fusce hendrerit nibh sed nunc faucibus viverra. Pellentesque imperdiet vitae lectus sit amet accumsan. Sed ultrices purus ac magna scelerisque blandit.
Pellentesque id ligula facilisis, mattis dui in, tincidunt est. Pellentesque at feugiat nibh. Morbi cursus malesuada urna, ac euismod urna condimentum nec. Aenean nec felis egestas, tincidunt elit non, blandit ex. Integer in malesuada tellus. Proin id mi ante. Fusce commodo risus sit amet ex lobortis, in porta augue facilisis. Curabitur viverra tortor in fringilla consequat. Etiam quis magna arcu. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus vulputate ex ac turpis dignissim, eget ultrices arcu condimentum. Duis risus nibh, vulputate eu urna nec, aliquet porttitor tortor.
Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Cras condimentum condimentum justo, id ultrices mauris fringilla eget. Quisque enim libero, varius et vehicula vel, faucibus nec massa. Vivamus in auctor justo. Suspendisse consequat nibh ac quam consectetur scelerisque. Quisque magna ex, ultrices hendrerit dictum a, sollicitudin gravida metus. Suspendisse metus nunc, placerat eget tristique ac, ullamcorper sit amet libero. Ut lacinia ultricies massa eget interdum.
Etiam tincidunt egestas velit, ac ullamcorper purus pharetra ac. Fusce porttitor augue vitae erat imperdiet, quis rutrum nibh euismod. Integer nec dui eget lorem dictum hendrerit at non lacus. Curabitur ultricies blandit orci, et aliquet magna ultricies a. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. In felis sem, consequat at ex vel, faucibus consectetur lectus. Nulla sed vestibulum massa. Donec ac orci in nunc ullamcorper tincidunt quis vel tortor. Donec aliquam, libero eu porttitor semper, neque eros interdum erat, fringilla ultrices magna sapien id lectus. Vivamus eget magna eu nibh egestas dapibus. Mauris dui orci, volutpat rutrum augue quis, scelerisque malesuada enim. Fusce ullamcorper turpis vestibulum metus luctus convallis. Nunc odio justo, suscipit vitae sapien in, pulvinar varius eros. Suspendisse id urna sem. 
"""
def simplest_func(a, b):
    """Old function
    
    >>> simplest_func(42, 42)
    84
    
    >>> simplest_func(-42, 42)
    0

    >>> simplest_func('', 42)
    Traceback (most recent call last):
    ...
    AssertionError: First argument is not int or float
    
    """
    assert isinstance(a, (int, float)), 'First argument is not int or float'
    assert isinstance(b, (int, float)), 'Second argument is not int or float'
    return a + b

def terrible_func(a, b):
    """Sum function of two ints or floats
    
    :param a: First number
    :type a: int or float
    :param b: Second number
    :type b: int or float
    :return: Sum of a and b
    :rtype: int or float
    
    """
    new_a = ''
    new_b = ''
    result = 0
    if (not isinstance(a, int)):
        while (not isinstance(new_a, int)):
            try:
                new_a = int(input('Submit a new value: '))
            except ValueError as error:
                print('Invalid argument!', error)
        result += new_a
    else:
        result += a
        
    if (not isinstance(b, int)):
        while (not isinstance(new_b, int)):
            try:
                new_b = int(input('Submit a new value: '))
            except ValueError as error:
                print('Invalid argument!', error)
        result += new_b
    else:
        result += b
        
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)