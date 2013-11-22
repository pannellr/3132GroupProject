#!/usr/bin/env python

import sys
sys.path.append('../singleton')
from singleton import Singleton
import MySQLdb
<<<<<<< HEAD
class Database:

    #values needed to establish connection
    database_name = ''
    database_user = ''
    database_pass = ''
    database_host = ''
    database_handle = ''
    _builder=None
=======
from querydirector import QueryDirector

class Database:

    #values needed to establish connection
    database_name = None
    database_user = None
    database_pass = None
    database_host = None
    database_handle = None
>>>>>>> af887552ca4845525d19d00cb2994eb76abdf538

    def __init__(self, name=None, user=None, password=None, host=None):
        self.database_name = name
        self.database_user = user
        self.database_pass = password
        self.database_host = host
        self.database_handle = Singleton()

    def connect(self):
        self.database_handle.setInstance(MySQLdb.connect(self.database_host,
                                               self.database_user,
                                               self.database_pass,
                                               self.database_name
<<<<<<< HEAD
                                               )
    def select(self):
        if !self._builder:
            self._builder=SelectBuilder()
        return self._builder
=======
                                               ))

    def execute(self, querybuilder):
        director = QueryDirector(querybuilder)
        self.database_handle.getInstance().query(director.getQuery())
        results = self.database_handle.getInstance().store_result()
        return results


    
>>>>>>> af887552ca4845525d19d00cb2994eb76abdf538
    
    def insert():
        
    def delete():
        
    def update():
        
