#!/usr/bin/env python

from querybuilder import QueryBuilder
from statement import Statement

class SelectBuilder(QueryBuilder):

    def __init__(self):
        self.statment = Statement()
        self.tables = Tables()
        self.where = Where()
        self.group = Group()
        self.order = Order()
        self.limit = Limit()

    def setStatement(self, statement):
        self.statement.string = statement
    
    def getStatement(self):
        return self.statement.string


    def setTables(self, tables):
        self.tables.string = tables
    
        
    def getTables(self): pass
    def getWhere(self): pass
    def getGroup(self): pass
    def getOrder(self): pass
    def getLimit(self): pass
    
