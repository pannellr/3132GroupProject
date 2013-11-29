#!/local/bin/python

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

    def __init__(self, args=None):
        self._post = Post()
        

    def show(self, args=None):
        post_id = None
        api = False
        if args:
          if 'post_id' in args.keys():
              post_id = args['post_id']
          if 'api' in args.keys():
              api = True
              
        posts = None
        content = None
        
        if post_id:
            posts = self._post.fetch(post_id)
        else:
            posts = self._post.all()
        

        if api:
            posts_dict = dict()
            while True:
                post = posts.fetch_row(1,1)
                if not post: break
                posts_dict[post[0]['post_id']] = {
                    'post_id' : post[0]['post_id'],
                    'user_id' : post[0]['user_id'],
                    'lat' : str(post[0]['lat']),
                    'lng' : str(post[0]['lng']),
                    'post' : post[0]['post'],
                    'created_at' : str(post[0]['created_at'])
                    }

            content = json.dumps(posts_dict)

            
        else:
            content = self.markup(posts)

        print content

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
        
