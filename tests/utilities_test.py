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

        # Lists
        self.assertTrue(is_of_list([]))
        self.assertTrue(is_of_list([1, 2]))
        self.assertTrue(is_of_list((1, 2)))
        self.assertFalse(is_of_list('test'))
        self.assertFalse(is_of_list(1))

        # Functions
        self.assertTrue(is_func(open))
        self.assertTrue(is_func(lambda x: x.upper()))
        self.assertFalse(is_func('test'))
        self.assertFalse(is_func(1))
        self.assertFalse(is_func([1, 2]))

        # Parse lambda
        normal = lambda x: x.upper()
        parsed = parse_lambda('lambda x: x.upper()')
        self.assertEqual(normal('a'), parsed('a'))

        self.assertIsNone(parse_lambda('3 + 2'))

        # Get index
        self.assertEqual(0, get_index(['test'], 'test'))
        self.assertEqual(14, get_index(['test'], 'inexistant', 14))
        self.assertIsNone(get_index(['test'], 'inexistant'))
