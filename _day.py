import unittest

class MyTestCase(unittest.TestCase):
    def test_something(self):
        filename = "./data/day1.txt"

        answer = 0

        with open(filename) as f:
            for line in f:
                yield line

        self.assertEqual(1, answer)

if __name__ == '__main__':
    unittest.main()