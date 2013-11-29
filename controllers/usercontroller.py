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
        _session = None

        def __init__(self):
            #Instantiates
                    self._user = User()
                    #Instantiated from superclasss
                    super(UserController, self).__init__()

                    #Gets the username/password from the form and attempts to login
                    def login(self, args):
                        #If the username entered in the form returns a password equivalent to the one entered
                        if (user.return_pw(args['user_name']) == args['password'])
                        #Sets the user_id = as the returned user_id given the user_name
                        user_id = self._user.return_user_id(args['user_name'])
                        #Creates a new session using UserID
                        self._session.setCookie(user_id)
                        _user.notify()

                        #Logs the current user out
                        def logout(self, args):
                            #If a session exist for a user nullify it
                            if session.getState()
                            _session.setCookie()
                            _user.notify()
        

