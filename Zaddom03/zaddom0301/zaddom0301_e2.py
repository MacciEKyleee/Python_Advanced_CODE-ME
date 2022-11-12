# Maciej Cieszyński

def number_of_digits(numbers):
    # numbers_element = [len(str(abs(x))) for x in numbers]
    tuple_list = [(x,len(str(abs(x)))) for x in numbers]

    # tuple_list = [(x,y) for x in numbers for y in numbers_element if ]

    # return numbers_element
    return tuple_list


if __name__ == '__main__':
    numbers = [91111, -7108079251, 4, 7942725602, -345220, 2915371507, -30, 9438104, 5736286, 984, 0]

    print(number_of_digits(numbers))
