#!/local/bin/python

import cgi,cgitb
cgitb.enable()
import imports
from mastercontroller import MasterController
from postcontroller import PostController

#import header and footer
header = open("header.html", "r").read()
footer = open("footer.html", "r").read()
body = open("body.html", "r").read()
            
url_args = cgi.FieldStorage()

c = PostController()

print "Content-Type: text/html"     # HTML is following
print                               # blank line, end of headers
print header

print c.show()


#body design
print body


print footer
