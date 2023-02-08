import unittest
from unittest.mock import Mock

from zaddom0401_e3 import three_times


class Zaddom0401_e3(unittest.TestCase):
    def test_correct_output_no_argument(self):
        func = Mock()
        decorated_func = three_times(func)
        decorated_func()

        self.assertEqual(func.call_count, 3)

    def test_correct_output_positional_argument(self):
        func = Mock()
        decorated_func = three_times(func)
        decorated_func('y')

        self.assertEqual(func.call_args_list[0].args[0] , 'y')
        self.assertEqual(func.call_args_list[1].args[0] , 'y')
        self.assertEqual(func.call_args_list[2].args[0] , 'y')


    def test_correct_output_keyword_argument(self):
        func = Mock()

        decorated_func = three_times(func)
        decorated_func(char='z')

        self.assertEqual(func.call_args_list[0].kwargs['char'] , 'z')
        self.assertEqual(func.call_args_list[1].kwargs['char'] , 'z')
        self.assertEqual(func.call_args_list[2].kwargs['char'] , 'z')


if __name__ == '__main__':
    unittest.main()
