#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------
# Scaffolder Tool
# -------------------------------------------------------------------
#
#
#   Author : PLIQUE Guillaume
#   Version : 1.0

# Dependencies
#=============
import os
import sys
import codecs
from .tools.renderer import Renderer
from .hub import Colifrapy
from .model import Model
from .tools.utilities import titler

# Template Directory
TEMPLATE_DIRECTORY = os.path.join(
    os.path.split(os.path.abspath(__file__))[0],
    'templates' + os.sep
)


# Main Class
#===========
class Scaffolder(Model):
    """ The Scaffolder is the base class that creates projects,
    model and generate necessary files from the templates. """

    # Tools
    renderer = Renderer(ignore=True)

    # Logger bootstrap
    def __init__(self):
        self.log.loadStrings(TEMPLATE_DIRECTORY + 'strings.yml')
        self.log.header('main:title')

    # Controller actions
    def new(self):

        # Folders to create
        folders = {
            'model' : True,
            'config' : False
        }

        # Files tp create
        files = {
            'main' : False,
            'controller': 'model/controller.py',
            'model' : 'model/example_model.py',
            'settings' : 'config/settings.yml',
            'strings'  : 'config/strings.yml',
            'readme'   : 'README.md',
            'gitignore': '.gitignore',
            'requirements' : 'requirements.txt'
        }

        # Options
        project_name = self.opts.target
        author = self.opts.author
        organization = self.opts.organization
        files['main'] = project_name + '.py'

        # Template variables
        template_vars = {'project': titler(project_name)}

        if author is not None:
            template_vars['author_line'] = '\n#   Author: %s' % author
        if organization is not None:
            template_vars['organization_line'] = '\n#   Organization: %s' % (
                organization)

        if self.opts.basic:
            files['basic'] = files.pop('main')

        # Announcing
        self.log.write('main:project', project_name)

        # Current Directory
        project_path = os.path.join(os.getcwd(), project_name + os.sep)
        if os.path.isdir(project_path):
            self.log.write('errors:existing')

        # Creating directories
        self.log.write('main:directory', project_path)
        os.makedirs(project_path)

        self.__moduleInit(project_path)
        for folder, module in list(folders.items()):
            self.log.write('main:directory', project_path + folder)
            os.makedirs(project_path + folder)

            # Initializing python module
            if module:
                self.__moduleInit(project_path + folder + os.sep)

        # Creating files
        for template, filename in list(files.items()):
            with codecs.open(project_path + filename, 'w+', 'utf-8') as f:
                self.log.write('main:file', project_path + filename)
                f.write(self.__render(template, template_vars))

        # Announcing the end
        self.log.write('main:end', project_name)

    def generate(self):
        
        # Options
        model_name = self.opts.target

    # Helpers
    def __moduleInit(self, path):
        with codecs.open(path + '__init__.py', 'w+', 'utf-8') as i:
            self.log.write('main:init', path)

    def __render(self, tpl, variables):
        with codecs.open(TEMPLATE_DIRECTORY + tpl + '.tpl', 'r', 'utf-8') \
              as tplf:
            return self.renderer.render(tplf.read(), variables)


# CLI Execution
# =============
class Hub(Colifrapy):
    pass

def main():
    hub = Hub(Scaffolder, TEMPLATE_DIRECTORY + 'settings.yml')

if __name__ == '__main__':
    main()
