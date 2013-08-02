# -------------------------------------------------------------------
# {{project}} Main Controller
# -------------------------------------------------------------------
#
#{{author_line}}
#   Version : 1.0

# Dependencies
#=============
from colifrapy import Model

# Main Class
#=============
class Controller(Model):

    # Example of controller action
    def test(self):
        self.log.write('main:test')