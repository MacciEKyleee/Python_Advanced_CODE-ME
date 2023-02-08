# imię i nazwisko
from random import randint


# tu napisz klasę Timed


def generate_and_sort(size):
    random_list = [randint(0, 1000) for _ in range(size)]
    sorted(random_list)


if __name__ == '__main__':
    generate_and_sort(1000)
    generate_and_sort(10000)
    generate_and_sort(100000)
