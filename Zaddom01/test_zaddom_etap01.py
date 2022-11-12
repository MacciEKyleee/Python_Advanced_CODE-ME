import unittest

from zaddom01 import MyTime


class TestEtap1(unittest.TestCase):
    def test_init(self):
        t = MyTime(10, 20)

        self.assertTrue(t.minutes == 10)
        self.assertTrue(t.seconds == 20)

        with self.assertRaises(ValueError):
            t = MyTime(10, 70)

        with self.assertRaises(ValueError):
            t = MyTime(10, -10)

        with self.assertRaises(ValueError):
            t = MyTime(-10, 10)

    def test_repr(self):
        t = MyTime(10, 20)

        self.assertTrue(t.__repr__() == 'MyTime(minutes=10, seconds=20)')


if __name__ == '__main__':
    unittest.main()
