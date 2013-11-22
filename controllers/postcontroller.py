#!/usr/bin/env python

from mastercontroller import MasterController
import json

class PostController(MasterController):

    _post = None

    def __init__(self):
        this._post = Post()

    def show(self, args):
        post_id = args['post_id']
        posts = None
        content = None
        
        if args['post_id']:
            posts = this._post.fetch(post_id)

        if args['api']:
            content = json.dumps(posts)
        else:
            content = this.markup(posts)

        return posts

    def new(self, args):
        #should we check permissions here?
        return this.markup(args)

    def create(self, args):
        _post.post(args['post'])
        #_post.user_id(args['user_id'])
        #_post.zone_id(fetch_zone_for(args['lat'], args['lng]
        _post.save()
        

    def edit(self, args):
        post_id = args['post_id']

    def update(self, args):
        post_id = args['post_id']
        post = args['post]
