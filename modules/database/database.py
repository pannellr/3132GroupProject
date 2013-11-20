#!/usr/bin/env python

import sys
sys.path.append('../singleton')
from singleton import Singleton
import MySQLdb
from querydirector import QueryDirector

class Database:

    #values needed to establish connection
    database_name = None
    database_user = None
    database_pass = None
    database_host = None
    database_handle = None

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
                                               ))

    def execute(self, querybuilder):
        director = QueryDirector(querybuilder)
        q = director.getQuery()
        print q


    
    
