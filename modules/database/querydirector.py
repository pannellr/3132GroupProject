#with help from https://gist.github.com/pazdera/1121157

from query import Query

class QueryDirector:

    __builder = None

    def __init__(self, builder):
        self.__builder = builder

    # Assemble the query
    def getQuery(self):
        query = Query()

        select = self.__builder.getStatement()
        query.setStatement(select)


        if self.__builder.commitMethod() == 'commit':
            values = self.__builder.getValues()
            query.setValues(values)
        else:
            tables = self.__builder.getTables()
            query.setTables(tables)

            where = self.__builder.getWhere()
            query.setWhere(where)

            group = self.__builder.getGroup()
            query.setGroup(group)

            order = self.__builder.getOrder()
            query.setOrder(order)

            limit = self.__builder.getLimit()
            query.setLimit(limit)

        return query.build()
