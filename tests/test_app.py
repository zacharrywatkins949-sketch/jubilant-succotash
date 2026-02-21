import unittest

class TestApp(unittest.TestCase):
    def test_example_one(self):
        self.assertEqual(1 + 1, 2)

    def test_example_two(self):
        self.assertTrue(isinstance('hello', str))

if __name__ == '__main__':
    unittest.main()