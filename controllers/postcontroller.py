#!//bin/env python

# add imports to path
import sys
sys.path.append('../')
import imports
# add json for API
import json
## import the Post model
from posts import Post
#import MasterController for inheritance
from mastercontroller import MasterController



class PostController(MasterController):

    _post = None

    def __init__(self):
        self._post = Post()

    def show(self, args=None):
        post_id = None
        api = False
        if args:
          if args['post_id']:  
              post_id = args['post_id']

          if args['api']:
              api = True
              
        posts = None
        content = None
        
        if post_id:
            posts = self._post.fetch(post_id)
        else:
            posts = self._post.all()
        

        if api:
            content = json.dumps(posts)
        else:
            content = self.markup(posts)

        print content


    def new(self, args):
        #should we check permissions here?
        return this.markup(args)

    def create(self, args):
        # Attach view to be updated
        self._post.attach(self.show())
        # set fields
        self._post.post(args['post'])
        #_post.user_id(args['user_id'])
        #_post.lat(args['lat'])
        #_post.lng(args['lng'])

        #save post
        self._post.save()
        
    def edit(self, args):
        post_id = args['post_id']

    def update(self, args):
        post_id = args['post_id']
        post = args['post']
        
