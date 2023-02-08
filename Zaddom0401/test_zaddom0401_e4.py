import unittest
from unittest.mock import Mock

from zaddom0401_e4 import many_times


class Zaddom0401_e4(unittest.TestCase):
    def test_decorator_function(self):
        func = Mock()
        repetitions = 10
        decorator = many_times(repetitions)
        decorated_func = decorator(func)

        decorated_func()

        self.assertEqual(func.call_count, repetitions)


if __name__ == '__main__':
    unittest.main()
