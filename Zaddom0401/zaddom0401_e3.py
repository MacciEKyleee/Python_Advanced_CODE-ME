# Maciej Cieszyński

def three_times(function):
    def wrapper(*args, **kwargs):
        for i in range(3):
            function(*args, **kwargs)
    return wrapper

@ three_times
def example_function(lang='EN'):
    if lang == 'PL':
        print("Ta linia została wydrukowana przez 'example_function'")
    elif lang == 'EN':
        print("This line is printed by the 'example_function'")
    else:
        raise NotImplementedError


if __name__ == '__main__':
    example_function()
    example_function('PL')
    example_function(lang='EN')
