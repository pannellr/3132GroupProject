#!/usr/bin/env python

from user import User
from subject import Subject


class User(Subject):
    _user_id = None
    _user_pw = None
    _user_email = None
	_verified = 0
	_online = 0
    
    def __init__(self, _user_id = None, _user_pw = None, user_email = None):
        super(User, self).__init__()
        self._user_id = _user_id
        self._user_pw = _user_pw
        self._user_email = _user_email
		self._verified = _verified
		self._online = _online

	#Returns the current user object
    def user(self):
        return self._user_id
	#Sets the current user objects
    def user(self, value):
        self._user_id = value
	#Returns the user ID of the current user
    def user_id(self):
        return self._user_id
	#Sets the user ID of the current user
    def user_id(self, value):
        self._user_id = value
	#Returns the email of the current user
    def email(self):
        return self._user_email	
	#Sets the email of the current user
    def email(self, email):
        _user_email = user_email
		
	#Returns the users online status
    def online(self):
        return self._online
	#Sets the user's online status
    def set_online(self, online):
        _online = 1
	#Sets the user's offline status
    def set_offline(self, online):
        _online = 1


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
    def return_pw()(self, user):
        select = SelectBuilder()
		select.setStatement('SELECT password')
		select.setTables('from posts')
		select.setWhere('where user_id="'+user.user_id()+'"')
		director = QueryDirector(select)
		
		try:
            this.user_pw_true = this._db.execute(director.getQuery())
        except:
            this._message('Could not locate password forthis user')
        self.notify()
		
	#Checks a user's password against the input username/password pair		
    def check_login()(self, user):
		select = SelectBuilder()
		select.setStatement('SELECT user_pw')
		select.setTables('posts')
		select.setWhere('user_id="'+user.user_id()+'"')
		director = QueryDirector(select)
        try:
            #this._db.query('SELECT user_pw FROM posts WHERE user_id ="'+user.user_id()'"')
			if (this._return_pw() = this._db.query(director.getQuery()))
				this._verified = 1
        except:
            this._message('incorrect password for this user')
        self.notify()
		
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
