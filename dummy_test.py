# Dummy test

import unittest


class TestDummy(unittest.TestCase):
    def test_dummy(self):
        self.assertEqual(1 + 1, 2)


if __name__ == '__main__':
    unittest.main()
