import sys
import unittest
from contextlib import contextmanager
from io import StringIO
from time import sleep

from zaddom0403_e2 import Timed


@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


class Zaddom0403_e2(unittest.TestCase):
    def test_timed_usage(self):
        with captured_output() as (out, err):
            with Timed() as timer:
                sleep(0.000001)

            output = out.getvalue().strip()

        time_without_milliseconds = output[:7]
        milliseconds = output[8:]

        self.assertEqual(time_without_milliseconds, '0:00:00')
        self.assertGreater(int(milliseconds), 0)
        self.assertNotEqual(int(milliseconds), 0)

    def test_ctx_man_returned_value(self):
        with Timed() as timer:
            pass

        self.assertTrue(isinstance(timer, Timed))

    def test_elapsed_usage(self):
        with captured_output() as (out, err):
            with Timed() as timer:
                sleep(0.000001)
                timer.elapsed()
                sleep(0.000001)

            output = out.getvalue().strip()

        time_values = output.split()

        self.assertEqual(time_values[0][:7], '0:00:00')
        self.assertNotEqual(int(time_values[0][8:]), 0)

        self.assertLess(int(time_values[0][8:]), int(time_values[1][8:]))


if __name__ == '__main__':
    unittest.main()
