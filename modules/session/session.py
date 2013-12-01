#!/usr/bin/env python

import Cookie
import os
import datetime
import random
#from State import *
		
class Session(object):

    def __init__(self, user = None):
        #print "session made!"
        
        self.state = None
        global cookie
        cookie = Cookie.SimpleCookie()
        print cookie
        if user is not None:
            self.user_id = user.user_id
            self.user_name = user.user_name
            cookie['user_id']=user.user_id
            cookie['user_id']['expires']=1*1*1*10*60

    def getState(self):
        #string_cookie = os.environ.get('HTTP_COOKIE')
        # If new session
        print cookie
        if cookie:
        #self.state = Expiredstate()
        #state.process(user)
            return False
        else:
            print cookie
            #self.state = Activestate()
            #state.process(user)
            return True
   
    def setCookie(self, num):
        cookie['user_id'] = num
        cookie['user_id']['expires']=1*1*1*10*5
        #print cookie['user_id'].value
    def getUserid(self):
        return cookie['user_id'].value
		
   
	
