#!/local/bin/python

import cgi,cgitb
cgitb.enable()
import imports
import os

from postcontroller import PostController
from commentcontroller import CommentController
from usercontroller import UserController
            
url_args = cgi.FieldStorage()

# map controller names to their classes
classes = {
    'user'    :  UserController,
    'post'    :  PostController,
    'comment' :  CommentController
    }

#build argument list
args = dict()

arg_keys = url_args.keys()

for key in arg_keys:
        args[key] = url_args.getvalue(key)

# get class name from url args
className = url_args.getvalue('class') if 'class' in url_args.keys() else 'post'

# get method from url -- defaults to show()
methodName = url_args.getvalue('method') if 'method' in url_args.keys() else 'show'

#call the class and method from the URL
getattr(classes[className](), methodName)(args)



