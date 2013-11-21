#!/usr/bin/env python

from subject import Subject

class Post(Subject):
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
        self.notify()

    def user_id(self):
        return self._user_id

    def user_id(self, value):
        self._user_id = value
        self.notify()

    def post_id(self):
        return self._post_id

    def post_id(self, post_id):
        self._post_id = post_id
        self.notify

    def zone_id(self):
        return self._zone_id

    def zone_id(self, lat, lng):
        self._zone_id = fetch_zone_for(lat, lng)
        self.notify()

    def fetch_zone_for(self, lat, lng):
        return 1

    # Database methods
    def all(self):
        all = None
        return all

    def fetch(self, post_id):
        post = None
        return post

    def update(self, post_id, fields):
        return True

    def delete(self, post_id):
        return True
