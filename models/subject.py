#!/usr/bin/env python

##with help from http://code.activestate.com/recipes/131499-observer-pattern/

import sys
sys.path.append('../modules/database')
from database import Database

class Subject():

    _observers = None
    _db = None
    _message = None
    
    def __init__(self):
        self._observers = []
        self._db = Database('pannell', 'pannell', 'B00609201', 'db.cs.dal.ca')
        serl.db.connect()

    def attach(self, observer):
        if not observer in self._observers:
            self._observers.append(observer)


    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)

    def message(self, message):
        this._message = message

    def message(self):
        return this._message
        
