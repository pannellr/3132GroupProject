#!/usr/bin/env python

from database import Database
from selectbuilder import SelectBuilder
from insertbuilder import InsertBuilder

d = Database('pannell', 'pannell',  'B00609201', 'db.cs.dal.ca')

d.connect()

print d.database_handle

select = SelectBuilder()

select.setStatement('select *')

print select.getStatement()

select.setTables('from users')

print select.getTables()

users = d.execute(select)
    
while True:
  record = users.fetch_row()
  if not record: break
  print record


insert = InsertBuilder()

insert.setStatement('insert into users (user_name, password, role) values ("p2p2p2", "4321", "normal")')

result = d.execute(insert)

