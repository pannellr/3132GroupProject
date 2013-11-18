#!/usr/bin/env python

from statement import Statement
from tables import Tables
from where import Where
from group import Group
from order import Order
from limit import Limit

class QueryBuilder:

    statement = None
    
    def getSelect(self): pass
    def getTables(self): pass
    def getWhere(self): pass
    def getGroup(self): pass
    def getOrder(self): pass
    def getLimit(self): pass
