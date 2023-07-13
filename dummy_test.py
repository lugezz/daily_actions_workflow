# Dummy test

import unittest


class TestDummy(unittest.TestCase):
    def test_dummy_1(self):
        self.assertEqual(1 + 1, 2)

    def test_dummy_2(self):
        self.assertEqual(10 + 1, 11)


if __name__ == '__main__':
    unittest.main()
