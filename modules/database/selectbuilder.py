#!/usr/bin/env python

from querybuilder import QueryBuilder
from statement import Statement
from tables import Tables
from where import Where
from group import Group
from order import Order
from limit import Limit

class SelectBuilder(QueryBuilder):


    def __init__(self):
        self.statement = Statement()
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
    
    def getTables(self):
        return self.tables.string
        
    def getWhere(self):
        return self.where.string

    def setWhere(self, where):
        self.where.string = where
        
    def getGroup(self):
        return self.group.string

    def setGroup(self, group):
        self.group.string = group
        
    def getOrder(self):
        return self.order.string
    
    def setOrder(self, order):
        self.order.string = order
        
    def getLimit(self):
        return self.limit.string

    def setLimit(self):
        self.limit.string = self
    
