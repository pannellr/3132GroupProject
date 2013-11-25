#!/local/bin/python

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
        conn = MySQLdb.connect(self.database_host, self.database_user, self.database_pass, self.database_name)
        self.database_handle.setInstance(conn)

    def execute(self, querybuilder):
        results = None
        director = QueryDirector(querybuilder)
        self.database_handle.getInstance().query(director.getQuery())
        if (querybuilder.commitMethod() == 'commit'):
            results = self.database_handle.getInstance().commit()
        else:
            results = self.database_handle.getInstance().store_result()
        return results


    
    
