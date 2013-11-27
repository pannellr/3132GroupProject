#!/local/bin/python

# add imports to path
import sys
sys.path.append('../')
import imports

# import json for API
import json

# import comment model
from comment import Comment

from mastercontroller import MasterController

class CommentController(MasterController):

    _comments = None
    
    def __init__(self, comments = None):
        self._comments = comments
