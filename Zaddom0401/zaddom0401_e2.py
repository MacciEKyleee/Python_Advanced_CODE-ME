# Maciej Cieszyński

def three_times(function):
    def wrapper():
        for i in range(3):
            function()
    return wrapper


@three_times
def example_function():
    print("This line is printed by the 'example_function'")


if __name__ == '__main__':
    example_function()
