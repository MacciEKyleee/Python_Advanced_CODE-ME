# Maciej Cieszyński

def three_times(param):
    # def wraper():
    #     example_function()
    #     example_function()
    #     example_function()
    # return wraper
    for i in range(3):
        result = param()
    return result


#@three_times
def example_function():
    print("This line is printed by the 'example_function'")


if __name__ == '__main__':
    three_times(example_function)
