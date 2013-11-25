#!/usr/bin/env python

from querybuilder import QueryBuilder
from statement import Statement
from tables import Tables


class InsertBuilder(QueryBuilder):


    def __init__(self):
        self.statement = Statement()
        self.tables = Tables()


    def setStatement(self, statement):
        self.statement.string = statement
    
    def getStatement(self):
        return self.statement.string

    def setTables(self, tables):
        self.tables.string = tables
    
    def getTables(self):
        return self.tables.string
     
    def commitMethod(self):
        return 'commit'
