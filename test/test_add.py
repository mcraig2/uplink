import os
import sys
import unittest

sys.path.insert(0, os.path.abspath('..'))
from uplink.add_entry import add_entry

class TestAddEntry(unittest.TestCase):
    def test_one_one(self):
        self.assertEqual(1 + 1, 2)


if __name__ == '__main__':
    unittest.main()
