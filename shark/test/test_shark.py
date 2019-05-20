'''
Brief:               Testing shows that sharks are fish

Author:              Simon Rydell
Python Version:      3.7
'''

import unittest
import shark

class TestSharks(unittest.TestCase):
    """All the shark tests"""

    def test_wrap_shark(self):
        """Test for wrap_shark function"""

        self.assertEqual(shark.wrap_shark(103), f"103, {'doo ' * 6}\n")

    def test_list_wrap_shark(self):
        """Test for wrap_shark function"""

        self.assertEqual(shark.wrap_shark([-123, 'and a string!']),
                         f"[-123, 'and a string!'], {'doo ' * 6}\n")

    def test_get_sharks(self):
        """ Don't care about the sharks, as long as there are 9 of them """

        self.assertEqual(9, len(shark.get_sharks()))
