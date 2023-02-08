# Maciej Cieszyński

def many_times(function, repetitions=5):
    def wrapper(*args, **kwargs):
        for i in range(repetitions):
            function(*args, **kwargs)
    return wrapper

@ many_times
def example_function(lang='EN'):
    if lang == 'PL':
        print("Ta linia została wydrukowana przez 'example_function'")
    elif lang == 'EN':
        print("This line is printed by the 'example_function'")
    else:
        raise NotImplementedError


if __name__ == '__main__':
    example_function('PL')
