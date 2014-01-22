# -------------------------------------------------------------------
# Colifrapy Utilities Tests
# -------------------------------------------------------------------
#
#
#   Author : Guillaume PLIQUE
#   Version : 0.1.0

# Dependencies
#=============
import unittest
from colifrapy.tools.utilities import *

# Main Test
#==========
class UtilitiesTest(unittest.TestCase):

    def test_types(self):

        # Strings
        self.assertTrue(is_string('test'))
        self.assertTrue(is_string(u'test'))
        self.assertFalse(is_string(13))
        self.assertFalse(is_string([1, 2]))

        # Numbers
        self.assertTrue(is_number(2))
        self.assertTrue(is_number(0))
        self.assertTrue(is_number(34.2))
        self.assertFalse(is_number(False))
        self.assertFalse(is_number('test'))
        self.assertFalse(is_number([1, 2]))
