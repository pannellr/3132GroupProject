class State:
    _state = None
    def __init__(self):
        self._state = None
    def process( self ):
       raise NotImplementedError
    def __str__( self ):
       return self.__doc__
		 
class ActiveState(State):
    def __init__(self):
        State.__init__(self)
    def process(self):
      #print "User ID  = %s" % user.user_id 
      #print "logged in"
        self._state = "Active"
        return True
	
	
class ExpireState(State):
    def __init__(self):
        State.__init__(self)
   
    def process(self):
      #print "User ID  = %s" % user.user_id 
      #print "not logged in"
        self._state = "Expired"
        return False