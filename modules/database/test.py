#!/usr/bin/env python

from database import Database
from selectbuilder import SelectBuilder

d = Database('pannell', 'pannell',  'B00609201', 'db.cs.dal.ca')

d.connect()

print d.database_handle

select = SelectBuilder()

select.setStatement('select * from')

print select.getStatement()

select.setTables('from users')

print select.getTables()

