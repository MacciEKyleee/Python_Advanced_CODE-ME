import sys
import unittest
from contextlib import contextmanager
from io import StringIO
from time import sleep

from zaddom0403_e1 import Timed


@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


class Zaddom0403_e1(unittest.TestCase):
    def test_timed_usage(self):
        with captured_output() as (out, err):
            with Timed():
                sleep(0.000001)

            output = out.getvalue().strip()

        time_without_milliseconds = output[:7]
        milliseconds = output[8:]

        self.assertEqual(time_without_milliseconds, '0:00:00')
        self.assertGreater(int(milliseconds), 0)
        self.assertNotEqual(int(milliseconds), 0)


if __name__ == '__main__':
    unittest.main()
