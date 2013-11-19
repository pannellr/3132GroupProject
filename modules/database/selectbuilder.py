#!/usr/bin/env python

from querybuilder import QueryBuilder
from statement import Statement
from tables import Tables
from where import Where
from group import Group
from order import Order
from limit import Limit

class SelectBuilder(QueryBuilder):

    statement = None
    tables = None
    where = None
    group = None
    order = None
    limit = None

    def __init__(self):
        self.statement = Statement()
        self.tables = Tables()
        self.where = Where()
        self.group = Group()
        self.order = Order()
        self.limit = Limit()

    def setStatement(self, statement):
        self.statement.setString(statement)
    
    def getStatement(self):
        return self.statement.getString()

    def setTables(self, tables):
        self.tables.string = tables
    
    def getTables(self):
        return self.tables.getString()
        
    def getWhere(self): pass
    def getGroup(self): pass
    def getOrder(self): pass
    def getLimit(self): pass
    
