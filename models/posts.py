#!/usr/bin/env python

from subject import Subject

class Post(Subject):
    _post_id = None
    _user_id = None
    _lat = None
    _lng = None
    _post = None

    
    def __init__(self, post_id=None, post=None, user_id=None, lat=None, lng=None):
        #super(Post, self).__init__()
        self._post_id = post_id
        self._post = post
        self._user_id = user_id
        self._lat = lat
        self._lng = lng

    # Accesors
    def post(self):
        return self._post

    def post(self, value):
        self._post = value

    def user_id(self):
        return self._user_id

    def user_id(self, value):
        self._user_id = value

    def post_id(self):
        return self._post_id

    def post_id(self, post_id):
        self._post_id = post_id

    def lat(self, lat):
        self._lat = lat

    def lat(self):
        return self._lat

    def lng(self, lng):
        self._lng = lng

    def lng(self):
        return self._lng

    

    # Database methods
    def all(self):
        posts = self._db.query('select * from posts')
        return posts

    def fetch(self, post_id):
        post = self._db.query('select * from posts where post_id = ' + post_id)
        return post

    def save(self):
        if self._post_id:
            self.update(self)
        else:
            try:
                self._db.query('insert into posts (user_id, post, lat, lng) values ("1", "' + self._post() + '" , "44.34567", "-66.78945")').commit()
            except: Exception, e: print repr(e)
                
        # notify upserver
#        self.notify()
        

    def update(self, post):
        try:
            self._db.query('update posts set user_id ="'+post.user_id()+'", post = "'+post.post()+'", lat ="'+post.lat()+'", lng = "'+post.lng()+'" where post_id = "' + post.post_id()).commit()
        except:
            #self.setMessage('Post could not be updated')
            print "query failed"
            
 #       self.notify()

    def delete(self, post_id):
        self._db.query('delete from posts where post_id = ' + post_id)
