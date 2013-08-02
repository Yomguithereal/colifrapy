# -------------------------------------------------------------------
# {{project}} Main Controller
# -------------------------------------------------------------------
#
#{{author_line}}
#   Version : 1.0

# Dependencies
#=============
from colifrapy import Model
from example_model import ExampleModel

# Main Class
#=============
class Controller(Model):
    
    # Properties
    example_model = None

    def __init__(self):
        self.example_model = ExampleModel()

    # Example of controller action
    def test(self):
        self.log.write('main:controller')
        self.example_model.hello()