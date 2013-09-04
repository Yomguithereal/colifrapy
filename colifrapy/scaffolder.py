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
from .tools.titler import titler

# Working Path
file_path = os.path.split(os.path.abspath(__file__))[0]+'/templates/'

# Main Class
#===========
class Scaffolder(Model):
    """ The Scaffolder is the base class that creates projects, model and generate
    necessary files to get going from the templates. """

    # Tools
    renderer = Renderer(ignore=False)
    project_name = False
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

    folders = {
        'model' : True,
        'config' : False
    }

    template_path = file_path
    template_vars = None

    # New Project
    def build(self, project, author=None, organization=None):
        self.log.write('main:start', variables={'project':project})

        self.files['main'] = project+'.py'
        self.project_name = project

        # Variables Assessment
        self.template_vars = {
            'project' : titler(project),
            'var' : '{{var}}'
        }

        # Options
        if author is not None:
            self.template_vars['author_line'] = '\n#   Author : '+author
        if organization is not None:
            self.template_vars['organization_line'] = '\n#   Organization : '+organization

        self.new_project()

        self.log.write('main:end', variables={'project':project})

    # Utilities
    def render(self, tpl):
        with codecs.open(self.template_path+tpl+'.tpl', 'r', 'utf-8') as tplf:
            return self.renderer.render(tplf.read(), self.template_vars)

    # Create __init__.py files
    def module_init(self, path):
        with codecs.open(path+'/__init__.py', 'w+', 'utf-8') as i:
            self.log.write('main:init', variables={'path':path})

    # File generation
    def new_project(self):

        # Current Directory
        project_path = os.getcwd()+'/'+self.project_name
        if os.path.isdir(project_path):
            self.log.write('errors:existing')

        # Creating directories
        self.log.write('main:directory', variables={'directory':project_path})
        os.mkdir(project_path)
        self.module_init(project_path)
        for folder, module in list(self.folders.items()):
            self.log.write('main:directory', variables={'directory':project_path+'/'+folder})
            os.mkdir(project_path+'/'+folder)

            # Initializing python module
            if module:
                self.module_init(project_path+'/'+folder)

        # Creating files
        for template, filename in list(self.files.items()):
            with codecs.open(project_path+'/'+filename, 'w+', 'utf-8') as f:
                self.log.write('main:file', variables={'file':project_path+'/'+filename})
                f.write(self.render(template))


# Command Line Execution
#=======================
class Hub(Colifrapy):

    # Launching Scaffolder
    def launch(self):
        self.log.load_strings(file_path+'strings.yml')
        self.log.header('main:title')

        self.controller.build(self.opts.project, self.opts.author, self.opts.organization)

def main():
    hub = Hub(Scaffolder, file_path+'settings.yml')
    hub.launch()

if __name__ == '__main__':
    main()