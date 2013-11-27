#!/local/bin/python

import cgi,cgitb
cgitb.enable()
import imports

from postcontroller import PostController
from commentcontroller import CommentController
from usercontroller import UserController
# need code
#from user import User
#from session import Session

#create session and user
# user = User()
# session = Sesion()

#import header and footer
header = open("header.html", "r").read()
footer = open("footer.html", "r").read()
            
url_args = cgi.FieldStorage()

# map controller names to their classes
classes = {
    'user'    :  UserController,
    'post'    :  PostController,
    'comment' :  CommentController
    }


parameters = None
controllerName = None

# get class name from url args
className = url_args.getvalue('class') if 'class' in url_args.keys() else 'post'
# defaults fo PostController
controller = classes[className]()
# get method from url -- defaults to show()
methodName = url_args.getvalue('method') if 'method' in url_args.keys() else 'show'

#build argument list
args = dict()

arg_keys = url_args.keys()

for key in arg_keys:
    args[key] = url_args.getvalue(key)

# add user and session to args dict for perm checking and state checking
#args['user'] = user;
#args['session'] = session;

if className == 'post' and methodName == 'show':
    print "Content-Type: text/html"     # HTML is following
    print                               # blank line, end of headers
    print header

#call the class and method from the URL
getattr(controller, methodName)(args)

#print url_args

if className == 'Post' and methodName == 'show':
    print footer
