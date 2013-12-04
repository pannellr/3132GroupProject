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
        super(PostController, self).__init__()
        self._post = Post()
        

    def show(self, args=None):
        posts = None
        post_id = None
        api = False
        if args:
          if 'post_id' in args.keys():
              post_id = args['post_id']
          if 'api' in args.keys():
              api = True
              
        posts = None
        content = ''
        
        posts = self._post.all()

        print 'Content-Type: text/html\n'
        print
        
        if api:
            content = json.dumps(posts)
        else:
            content += self.HEADER
            content += self.markup(posts)
            content += self.FOOTER

        print content

    def create(self, args):
        # Attach view to be updated
        self._post.attach(PostController)
        # set fields
        self._post.post(args['post'])
        self._post.user_id(args['user_id'])
        #_post.lat(args['lat'])
        #_post.lng(args['lng'])

        #save post
        self._post.save()
        
    def delete(self, args):
        self._post.attach(PostController)
        self._post.destroy(args['post_id'])


        
