from designPatterns.python.singleton import main_singletons
import unittest
import os
import sys

sys.path.append(os.getcwd())


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
