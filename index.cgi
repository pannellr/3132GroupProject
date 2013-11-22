#!/usr/bin/env python

import cgi,cgitb
cgitb.enable()

#import header and footer
header = open("header.html", "r").read()
footer = open("footer.html", "r").read()
body = open("body.html", "r").read()
            
url_args = cgi.FieldStorage()

print "Content-Type: text/html"     # HTML is following
print                               # blank line, end of headers
print header

#body design
print body


print footer
