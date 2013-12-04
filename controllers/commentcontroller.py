#!/local/bin/python

# add imports to path
import sys
sys.path.append('../')
import imports

from postcontroller import PostController

# import json for API
import json

# import comment model
from comment import Comment

from mastercontroller import MasterController

class CommentController(MasterController):

    _comment = None
    
    def __init__(self, comments = None):
        self._comment = Comment()
        super(CommentController, self).__init__()

    def create(self, args):
        self._comment.attach(PostController)

        self._comment.user_id(args['user_id'])
        self._comment.post_id(args['post_id'])
        self._comment.comment(args['comment'])
        self._comment.save()
