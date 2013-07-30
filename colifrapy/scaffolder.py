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
from logger import Logger
from settings import Settings
from commander import Commander
from model import Model

# Working Path
file_path = os.path.split(os.path.abspath(__file__))[0]+'/templates/'

# Main Class
#===========
class Scaffolder(Model):

    # Tools
    files = {
        'main' : False,
        'controller': 'model/controller.py',
        'settings' : 'config/settings.yml',
        'strings'  : 'config/strings.yml',
        'readme'   : 'README.md',
        'gitignore': '.gitignore'
    }

    folders = [
        'model',
        'config'
    ]

    template_path = file_path
    template_vars = None

    # Constructor
    def __init__(self, project, author='Author'):
        self.log.write('main:start', variables={'project':project})
        
        self.files['main'] = project+'.py'
        self.template_vars = {'project' : project, 'author' : author}
        self.new_project()
       
        self.log.write('main:end', variables={'project':project})

    # Utilities
    def render(self, tpl):
        with codecs.open(self.template_path+tpl+'.tpl', 'r', 'utf-8') as tplf:
            return pystache.render(tplf.read(), self.template_vars)
    
    # File generation
    def new_project(self):

        # Current Directory
        project_path = os.getcwd()+'/'+self.template_vars['project']
        if os.path.isdir(project_path):
            self.log.write('errors:existing')

        # Creating directories
        self.log.write('main:directory', variables={'directory':project_path})
        os.mkdir(project_path)
        for folder in self.folders:
            self.log.write('main:directory', variables={'directory':project_path+'/'+folder})
            os.mkdir(project_path+'/'+folder)

        # Creating files
        for template, filename in self.files.iteritems():
            with open(project_path+'/'+filename, 'w+') as f:
                self.log.write('main:file', variables={'file':project_path+'/'+filename})
                f.write(self.render(template))


# Command Line Execution
#=======================
if __name__ == '__main__':

    # Launching Colifrapy
    settings = Settings()
    settings.load(file_path+'settings.yml')
    logger = Logger()
    logger.load_strings(file_path+'strings.yml')
    commander = Commander()

    # Launching Scaffolder
    logger.header('main:title')

    if commander.opts.action != "new":
        logger.write('errors:action')
    else:
        scaffold = Scaffolder(commander.opts.project, commander.opts.author)