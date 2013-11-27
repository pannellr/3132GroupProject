#!/usr/bin/env python
from Session import *
class User(object):
   user_name = None
   user_id = None
   def __init__(self, name, id):
      self.user_name = name
      self.user_id = id
user = User("vivian",2)
session = Session(user)
print session.getUserid()
condition = session.getState()
print(condition)
if condition:
	id = session.getUserid()
	user = User("vivian", id)
	print(user.user_id)
	print("cookie works!")
else:
	user = User("vivian", 1)
	print(user.user_id)
