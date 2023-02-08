import unittest
from unittest.mock import Mock

from zaddom0401_e2 import three_times


class Zaddom0401_e2(unittest.TestCase):
    def test_called_three_times(self):
        func = Mock()
        decorated_func = three_times(func)
        decorated_func()

        self.assertEqual(func.call_count, 3)


if __name__ == '__main__':
    unittest.main()
