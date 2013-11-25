#!/usr/bin/env python

import sys
sys.path.append('../')
import imports

from posts import Post

#import json
from mastercontroller import MasterController



class PostController(MasterController):

    _post = None

    def __init__(self):
        self._post = Post()

    def show(self, args=None):
        post_id = None
        if args:
          post_id = args['post_id']
        posts = None
        content = None
        
        if post_id:
            posts = self._post.fetch(post_id)
        else:
            posts = self._post.all()
        

        if args['api']:
            content = json.dumps(posts)
        else:
            content = self.markup(posts)

        return posts


    def new(self, args):
        #should we check permissions here?
        return this.markup(args)

    def create(self, args):
        # Attach view to be updated
        _post.attach('show')
        # set fields
        _post.post(args['post'])
        _post.user_id(args['user_id'])
        _post.lat(args['lat'])
        _post.lng(args['lng'])

        #save post
        _post.save()
        
    def edit(self, args):
        post_id = args['post_id']

    def update(self, args):
        post_id = args['post_id']
        post = args['post']
        
