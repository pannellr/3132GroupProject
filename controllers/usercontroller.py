#!/local/bin/python

# add imports to path
import sys
sys.path.append('../')
import imports
# add json for API
import json
#imort the user model
from user import User
# imort MasterControler for inheritance
from mastercontroller import MasterController

class UserController(MasterController):

    _user = None


    def login(self, args):
        

