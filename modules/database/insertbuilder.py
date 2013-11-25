#!/usr/bin/env python

from querybuilder import QueryBuilder
from statement import Statement
from values import Values

class InsertBuilder(QueryBuilder):


    def __init__(self):
        self.statement = Statement()
        self.values = Values()
        
    def setStatement(self, statement):
        self.statement.string = statement
    
    def getStatement(self):
        return self.statement.string

    
    def setValues(self, values):
        self.values.string  = values

    def getValues(self):
        return self.values.string
   
    
