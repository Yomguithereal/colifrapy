# -*- coding: utf-8 -*-
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
            'this is a test and a second ',
            self.renderer.render(
                'this is a {{var1}} and a second {{var2}}',
                'test'
            )
        )

        self.assertEqual(
            'this is a unicode string',
            self.renderer.render('this is a {{var}} string', u'unicode')
        )

        self.assertEqual(
            u'this is a accentuated dépression',
            self.renderer.render('this is a accentuated {{var}}', u'dépression')
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
        self.assertEqual(
            'bananas are good',
            self.renderer.render(
                '{{var1}} are {{var2}}',
                {'var1': 'bananas', 'var2': 'good'}
            )
        )

    def test_escaping(self):

        # Basic
        self.assertEqual(
            'escaped %2C url',
            self.renderer.render('escaped {{var}} url', '%2C')
        )

        self.assertEqual(
            'escaped %2C url and second also ',
            self.renderer.render(
                'escaped {{var}} url and second also {{var}}',
                '%2C'
            )
        )

        self.assertEqual(
            'escaped aztec.test',
            self.renderer.render('escaped {{re_escaping}}', 'aztec.test')
        )

        self.assertEqual(
            'escaped aztec.foo and aztec.bar',
            self.ignore_renderer.render(
                'escaped {{re1}} and {{re2}}',
                ('aztec.foo', 'aztec.bar')
            )
        )
