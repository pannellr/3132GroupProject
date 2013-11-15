#with help from https://gist.github.com/pazdera/1121157

class QueryDirector:

    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder

    # Assemble the query
    def getQuery(self):
        query = Query()

        select = self.__builder.getSelect()
        query.setSelect(select)

        #from/join tables
        tables = self.__builder.getTables()
        query.setTables(tables)

        #where
        where = self.__builder.getWhere()
        query.setWhere(where)

        #group
        group = self.__builder.getGroup()
        query.setGroup(group)

        #order
        order = self.__builder.getOrder()
        query.setOrder(order)

        #limit
        limit = self.__builder.getLimit()
        query.getLimit()

        return query
