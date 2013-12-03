#!/local/bin/python

# add imports to path
import sys
sys.path.append('../')
import imports
## import the Post model
from users import User
#import MasterController for inheritance
from mastercontroller import MasterController
from postcontroller import PostController

class UserController(MasterController):

    _user = None

    def __init__(self, args=None):
        self._user = User()
        super(UserController, self).__init__()

    def login(self, args):

        password = self._user.return_pw(args['user_name'])
        if password['password'] == args['password']:
            self._user.load(args['user_name'])
            self._session.setCookie(self._user)

        print self._session._cookie
        self._user.attach(PostController)    
        self._user.notify()
            

    def logout(self, args):
        self._session.clearCookie()
        print self._session._cookie
        self._user.attach(PostController)
        self._user.notify()
