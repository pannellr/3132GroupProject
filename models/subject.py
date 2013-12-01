#!/local/bin/python

##with help from http://code.activestate.com/recipes/131499-observer-pattern/
import cgi
import sys
sys.path.append('../')
import imports

from database import Database
from selectbuilder import SelectBuilder
from insertbuilder import InsertBuilder

class Subject(object):

    _observers = None
    _db = None
    _message = None
    
    def __init__(self):
        self._observers = []
        self._db = Database('pannell', 'pannell', 'B00609201', 'db.cs.dal.ca')
        self._db.connect()

    def attach(self, observer):
        if not observer in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        url = "http://web.cs.dal.ca/~kou/3132GroupProject/"
        print "Status: 302 Moved"
        print "Location: %s" % url
        print
        
        #for observer in self._observers:
        #    if modifier != observer:
        #       print modifier
                

    def all(self, tableName):
        select = SelectBuilder()
        select.setStatement('select *')
        select.setTables('from ' + tableName)
        results = self._db.execute(select)
        return results


    #accesors for error messages
    def setMessage(self, m):
        self._message = m

    def message(self):
        return self._message
        
    
