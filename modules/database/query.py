class Query:

    def __init__(self):
        self.__statement = None
        self.__tables    = None
        self.__where     = None
        self.__group     = None
        self.__order     = None
        self.__limit     = None

    #statement generic covers delete/select/update/insert
    def setStatement(self, statement):
        self.__statement = statement

    def setTables(self, tables):
        self.__tables = tables

    def setWhere(self, where):
        self.__where = where

    def setGroup(self, group):
        self.__group = group

    def setOrder(self, order):
        self.__order = order

    def setLimit(self, limit):
        self.__limit = limit

    def build(self):
        q = self.__statement + ' ' + self.__tables

        if self.__where:
            q += ' ' + self.__where

        if self.__group:
            q += ' ' + self.__group

        if self.__order:
            q += ' ' + self.__order

        if self.__limit:
            q += ' ' + self.__limit

        return q
