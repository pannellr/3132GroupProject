#!/local/bin/python

import sys
sys.path.append('../')
import imports
import os

from Session import Session

class MasterController(object):

    #import header and footer
    HEADER = open("header.html", "r").read()
    FOOTER = open("footer.html", "r").read()
    URL_BASE = '/~pannell/3132GroupProject'
    
    _session = None

    def __init__(self):
        self._session = Session()

    def markup(self, posts):
        
        markup = ''
        markup += '<div id="wrap2">'
        markup += '<img border="0" src="' + self.URL_BASE + '/gglogo.png" alt="gogeo logo" width="250" height="125">'
        markup += '<img border="0" src="' + self.URL_BASE + '/banner.png" alt="banner" width="1000" height="125">'
        markup += '</div>'
        markup += '</br >'
        markup += '<div id="wrap">'
        markup += '<h3> Geo-Location </h3>'
        markup += '<div id="map">'
        markup += '</div>'
        markup += '</div>'

        markup += '<div id="wrap4">'

        print self._session._cookie
        if self._session.getState():
        
            markup += '<form action="' + self.URL_BASE + '/post/create" method="GET" class="post-form">'
            markup += '<p>'
            markup += '<label for="post">Post</label><br />'
            markup += '<textarea name="post" rows="5" cols="80"></textarea><br />'
            markup += '<input type="submit" value="Post" class="post-form-submit"/>'
            markup += '</p>'
            markup += '</form>'
            markup += '<div class="post-form-links"><a href="' + self.URL_BASE + '/user/logout">Logout</a></div>'

        else:

            markup += '<form action="' + self.URL_BASE + '/user/login" method="POST" class="login-form">'
            markup += '<p>'
            markup += '<label for="user_name">User Name</label><br />'
            markup += '<input name="user_name" />'
            markup += '</p>'
            markup += '<p>'
            markup += '<label for="password">Password</label><br />'
            markup += '<input type="password" name="password" />'
            markup += '</p>'
            markup += '<input type="submit" value="Login" class="login-form-submit"/>'
            markup += '</p>'
            markup += '</form>'
        
        
        while True:
            post = posts.fetch_row(1,1)
            if not post: break
            markup += '<div class="post-wrapper">'
            markup += '<span class="post-author">Author: '
            markup += str(post[0]['user_id'])
            markup += '</span>'
            markup += '<span class="post-location" data-lat="' + str(post[0]['lat']) + '" data-lng="' + str(post[0]['lng']) + '">'
            markup += 'lat: ' + str(post[0]['lat']) + ' lng: ' + str(post[0]['lng'])
            markup += '</span>'
            markup += '<div class="post-content">'
            markup += post[0]['post']
            markup += '</div>'
            markup += '<span class="post-date"><em>' + post[0]['created_at'].strftime('%m/%d/%Y') + '</em></span>'
            markup += '</div>'
            # add options here
            # markup += '<div class="post-links">"

            #check permissions and add delete, comment, and edit links here
            
            # markup += '</div>'

            markup += '<hr />'

        markup += '</div>'
        
        return markup
