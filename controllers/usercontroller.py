#!/local/bin/python

# add imports to path
import os, sys, time, cPickle

import cgi
import cgitb; cgitb.enable()
sys.path.append('../')
import imports
# add json for API
import json
#imort the user model
from user import User
# imort MasterControler for inheritance
from mastercontroller import MasterController

class UserController(MasterController):

    _user = None

    def __init__(self, user):
        self._user + user

	def show(self, args=None):
		url_args = cgi.FieldStorage()
        args = {x: url_args.getvalue(x) for x in url_args.keys()}

		print "Content-type: text/html\n"

        datafile = sys.argv[0]+'.data'

        if not os.path.exists(datafile):
			with open(datafile, "wb") as handle:
			cPickle.dump([],handle)

		with open(datafile, "rb") as handle:
			data = cPickle.load(handle)

		if 'comment' in args:
			data.append({
               'who' : args.get('user',""),
               'when': time.ctime(),
               'what': args.get('comment')
            })
			with open(datafile, "wb") as handle:
				cPickle.dump(data,handle)
    
print "<html><head></head><body>"
if args.get("user",""):
    print "<p>logged as %s</p>" % args["user"]
    print '''<form action="%s" method="get">
    <input type="hidden" name="user" value=""/>
    <input type="submit" value="Log out">
    </form>''' % sys.argv[0]
else:
    print '''<form action="%s" method="get">
    <input type="text" name="user">
    <input type="submit" value="Log in">
    </form>''' % sys.argv[0]
    
print "<h1>Comments:</h1><ul>"

for x in data:
    print "<li><b>%s <em>(%s)</em>:</b> %s</li>" % (x['who'], x['when'], x['what'])
print "</ul>"

print '''<form action="%s" method="get">
<input type="hidden" name="user" value="%s">
<input type="text" name="comment">
<input type="submit" value="Add comment">
</form>''' % (sys.argv[0], args.get("user",""),)

print "</body></html>"