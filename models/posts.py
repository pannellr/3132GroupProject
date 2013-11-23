#!/usr/bin/env python

from subject import Subject

class Post(Subject):
    _post_id = None
    _user_id = None
    _lat = None
    _lng = None
    _post = None

    
    def __init__(self, post_id=None, post=None, user_id=None, lat=None, lng=None):
        super(Post, self).__init__()
        self._post_id = post_id
        self._post = post
        self._user_id = user_id
        self._zone_id = self.fetch_zone_for(lat, lng)

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
        all = None
        return all

    def fetch(self, post_id):
        post = None
        return post

    def save(self, view):
        if this._post_id:
            this.update(self)
        else:
            try:
                this._db.query('insert into posts (user_id, post, lat, lng) values ("1",' + self._post() + ', "44.34567", "-66.78945")')
            except:
                this._message('Post could not be created')
        # notify upserver
        self.notify()
        

    def update(self, post):
        try:
            this._db.query('update posts set user_id ="'+post.user_id()+'", post = "'+post.post()+'", lat ="'+post.lat()+'", lng = "'+post.lng()+'" where post_id = "' + post.post_id())
        except:
            this._message('Post could not be updated')

        self.notify()

    def delete(self, post_id):
        return True
