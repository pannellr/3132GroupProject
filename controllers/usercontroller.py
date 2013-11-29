#!/local/bin/python

# add imports to path
import sys
sys.path.append('../')
import imports
## import the Post model
from users import User
#import MasterController for inheritance
from mastercontroller import MasterController

class UserController(MasterController):

    _user = None

    def __init__(self, args=None):
        self._user = User()

    def login(self, args):
        password = self._user.return_pw(args['user_name'])
        print password
        if password == args['password']:
            self._user.build()
            self._session.setCookie(self._user._user_id)

        self._user.notify()
            

    def logout(self, args):
        return True
