import unittest

import hello


class TestMethods(unittest.TestCase):
    def test_add(self):
        self.assertEqual(hello.say1(), "hello")
    def test_say(self):
        self.assertEqual(hello.say2(), "world")


if __name__ == '__main__':
    unittest.main()
