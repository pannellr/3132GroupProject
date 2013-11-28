#!/usr/bin/env python
from User import *
Class State(object):
   def process( self, user ):
        raise NotImplementedError
   def __str__( self ):
		return self.__doc__
		 
Class Activiestate(State):
   def process(user):
		print "User ID  = %s" % user.user_id 
		print "logged in"
		return
	
	
Class Expiredstate(State):
   def process(user):
		print "User ID  = %s" % user.user_id 
		print "not logged in"
		return