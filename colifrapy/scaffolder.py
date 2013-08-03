#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------
# Scaffolder Tool
# -------------------------------------------------------------------
#
#
#   Author : PLIQUE Guillaume
#   Version : 1.0

# Dependancies
#=============
import os
import sys
import codecs
import pystache
from hub import Colifrapy
from model import Model

# Working Path
file_path = os.path.split(os.path.abspath(__file__))[0]+'/templates/'

# Main Class
#===========
class Scaffolder(Model):

    # Tools
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
    def build(self, project, author=None):
        self.log.write('main:start', variables={'project':project})

        self.files['main'] = project+'.py'
        self.project_name = project

        # Variables Assessment
        if author is not None:
            author = '\n#   Author : '+author
        self.template_vars = {
            'project' : project.title(),
            'author_line' : author,
            'var' : '{{var}}'
        }
        self.new_project()

        self.log.write('main:end', variables={'project':project})

    # Utilities
    def render(self, tpl):
        with codecs.open(self.template_path+tpl+'.tpl', 'r', 'utf-8') as tplf:
            return pystache.render(tplf.read(), self.template_vars)

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
        for folder, module in self.folders.iteritems():
            self.log.write('main:directory', variables={'directory':project_path+'/'+folder})
            os.mkdir(project_path+'/'+folder)

            # Initializing python module
            if module:
                self.module_init(project_path+'/'+folder)

        # Creating files
        for template, filename in self.files.iteritems():
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

        if self.opts.action != "new":
            self.log.write('errors:action')
        else:
            self.controller.build(self.opts.project, self.opts.author)

def main():
    hub = Hub(Scaffolder, file_path+'settings.yml')
    hub.launch()

if __name__ == '__main__':
    main()