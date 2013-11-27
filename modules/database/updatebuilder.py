#!/usr/bin/env python

from querybuilder import QueryBuilder
from statement import Statement

class UpdateBuilder(QueryBuilder):


    def __init__(self):
        self.statement = Statement()

    def setStatement(self, statement):
        self.statement.string = statement
    
    def getStatement(self):
        return self.statement.string

     
