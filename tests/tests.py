from designPatterns.python.singleton import main_singletons
import unittest
import sys
import os


myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')


class TestBriefCase(unittest.TestCase):

    def test_assert(self):
        self.assertEqual(1, 1)

    def test_singletons(self):
        self.assertEqual(
            'Calling the singleton module!!',
            main_singletons.get_inmodule()
        )


if __name__ == '__main__':
    unittest.main()
