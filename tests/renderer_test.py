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
#==========
class RendererTest(unittest.TestCase):

    def setUp(self):
        self.renderer = Renderer()
        self.ignore_renderer = Renderer(ignore=True)

    def test_integer(self):
        self.assertEqual(
            '23 passed',
            self.renderer.render('{{int}} passed', 23)
        )

    def test_string(self):
        self.assertEqual(
            'this is a test',
            self.renderer.render('this is a {{var}}', 'test')
        )

        self.assertEqual(
            'this is a test and a second test',
            self.renderer.render(
                'this is a {{var1}} and a second {{var2}}',
                'test'
            )
        )

        self.assertEqual(
            'this is a unicode string',
            self.renderer.render('this is a {{var}} string', u'unicode')
        )

    def test_list(self):

        # List
        self.assertEqual(
            'this is a test',
            self.renderer.render('this {{verb}} a {{comp}}', ['is', 'test'])
        )

        # Tuple
        self.assertEqual(
            'this is a test',
            self.renderer.render('this {{verb}} a {{comp}}', ('is', 'test'))
        )

    def test_dict(self):
        pass

    def test_escaping(self):

        # Basic
        self.assertEqual(
            'escaped %2C url',
            self.renderer.render('escaped {{var}} url', '%2C')
        )

        self.assertEqual(
            'escaped %2C url and second also %2C',
            self.renderer.render(
                'escaped {{var}} url and second also {{var}}',
                '%2C'
            )
        )

        # With dictionaries
        # self.assertEqual(
        #     'escaped %2C url',
        #     self.renderer.render('escaped {{var}} url', {'var': '%2C'})
        # )

        # self.assertEqual(
        #     'escaped %2C url and second also %2C',
        #     self.renderer.render(
        #         'escaped {{var1}} url and second also {{var2}}',
        #         {'var1': '%2C', 'var2': '%2C'}
        #     )
        # )
