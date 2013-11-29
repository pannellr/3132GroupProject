#!/usr/bin/env python

from Session import session
from subject import Subject


class User(Subject):
    _user_id = None
    _user_pw = None
    _user_email = None
    _session = None;
    def __init__(self, _user_id = None, _user_pw = None, user_email = None):
        super(User, self).__init__()
        self._user_id = _user_id
        self._user_pw = _user_pw
        self._user_email = _user_email
		self._session = Session
		


    # Database methods
    def all(self):
        all = None
        return all
		
	#Sets a new user by adding it to the database
    def new_user(self, view):
		insert = InsertBuilder()
		insert.setStatement('INSERT INTO users (user_id, user_pw, user_email, online)')
		insert.setValues(self._user_id() + ',' + self._post + ',' + self._user_email() + ',' + self._online())
		director = QueryDirector(insert)
		
        if this._user_id:
            this.update(self)
        else:
            try:
				#Query for user data insertion
                this._db.query(director.getQuery())
            except:
                this._message('User could not be created')
        self.notify()
		
	#Returns a user's password		
		
	#Checks a user's password against the input username/password pair		
    def return_pw()(self, user_name=None):
		select = SelectBuilder()
		select.setStatement('SELECT password')
		select.setTables('from users')
		select.setWhere('where user_name = "'+user_name+'"')
		result = self._db.execute(select)
		password = result.fetch_row(1,1)
		return password[0]
		
	def return_user_id()(self, user_name=None):
		select = SelectBuilder()
		select.setStatement('SELECT user_id')
		select.setTables('from users')
		select.setWhere('where user_name = "'+user_name+'"')
		result = self._db.execute(select)
		user_id = result.fetch_row(1,1)
		return user_id[0]
		
	def return_user_role()(sefl, user_name=None):
		select = SelectBuilder()
		select.setStaement('SELECT role')
		selcet.setTables('from users')
		selcet.setWhere('where user_name = "'+user_name+'"')
		result = self._db.execute(select)
		
		
			 
		
	#Update	
    def update(self, user):
		update = UpdateBuilder()
		update.setStatement('UPDATE users SET user_id ="'+user.user_id()+'", user_pw = "'+user.get_user_pw()+'", user_email ="'+user.email()+'", online = "'+user.online()+'" WHERE user_id = "' + user.user_id())
        director = QueryDirector(update)
		try:
            this._db.query(director.getQuery())
        except:
			self.notify()
				this._message('User set')
		
	#Removes a user from the database	
    def delete_user(self, user):
		delete = DeleteBuilder()
		delete.setStatement('DELETE FROM user WHERE user_id = "'+user.user_id()'"')
		director = QueryDirector(delete)
        try:
            this._db.query(director.getQuery())
        except:
            this._message('No user to delete')
        self.notify()
	def 