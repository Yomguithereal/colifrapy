# -------------------------------------------------------------------
# Colifrapy Renderer Tests
# -------------------------------------------------------------------
#
#
#   Author : Guillaume PLIQUE
#   Version : 0.1.0

# Dependencies
#=============
import unittest
from colifrapy.tools.renderer import Renderer

# Main Test
#===========
class RendererTest(unittest.TestCase):

    def setUp(self):
        self.renderer = Renderer()
        self.ignore_renderer = Renderer(ignore=True)

    def test_integer(self):
        pass

    def test_string(self):
        pass

    def test_list(self):
        pass

    def test_dict(self):
        pass
