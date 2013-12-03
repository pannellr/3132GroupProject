#!/local/bin/python


import os
import Cookie
import datetime
import random
#from State import *
		
class Session(object):

    _cookie = None
    _session = None
    _user_id = None
    _user_name = None
    _role = None

    def __init__(self):
        cookie_string = os.environ['HTTP_COOKIE']
        self._cookie = Cookie.SimpleCookie()
        if cookie_string:
            self._cookie.load(cookie_string)
            if 'user_id' in self._cookie.keys():
                self._user_id = self._cookie['user_id'].value

    def getState(self):
        if self._user_id:
            return True
        else:
            return False


    def setCookie(self, user):
        expiration = datetime.datetime.now() + datetime.timedelta(days=30)
        self._cookie['session'] = random.randint(0,1000000000)
        self._cookie['user_id'] = user._user_id
        self._cookie['user_name'] = user._user_name
        self._cookie['role'] = user._role
        self._cookie['session']['expires'] = expiration.strftime("%a, %d-%b-%Y %H:%M:%S PST")
        
    def clearCookie(self):
         self._cookie['session'] = ''
         self._cookie['user_id'] = ''
         self._cookie['user_name'] = ''
         self._cookie['role'] = ''
         self._cookie['session']['expires'] = ''
         self._user_id = None
         self._user_name = None
         self._role = None
