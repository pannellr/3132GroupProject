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
            markup += '<input type="hidden" name="user_id" value="' + self._session._user_id + '"/>'
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
        
        
        for post_id in posts:
            markup += '<div class="post-wrapper">'
            markup += '<span class="post-author">Author: '
            markup += posts[post_id]['user_id']
            markup += '</span>'
            markup += '<span class="post-location" data-lat="' + posts[post_id]['lat'] + '" data-lng="' + posts[post_id]['lng'] + '">'
            markup += 'lat: ' + posts[post_id]['lat'] + ' lng: ' + posts[post_id]['lng']
            markup += '</span>'
            markup += '<div class="post-content">'
            markup += posts[post_id]['post']
            markup += '</div>'
            markup += '<span class="post-date"><em>' + posts[post_id]['created_at'] + '</em></span>'
            markup += '</div>'
            markup += '<div class="post-links">'

            if self._session._role == 'admin':
                markup += '<a href="' + self.URL_BASE + '/post/delete?post_id=' + str(post_id) + '">Delete this post</a>'


            markup += '</div>'
            markup += '<div class="comments_wrapper">'

            if posts[post_id]['comments']:
                markup += '<h4>Comments:</h4>'

            for comment_id in posts[post_id]['comments']:
                markup += '<div class="comment-wrapper">'
                markup += '<p>' + posts[post_id]['comments'][comment_id]['comment'] + '</p>'
            

            if self._session.getState():
                markup += '<div class="comment-form">'
                markup += '<form action="' + self.URL_BASE + '/comment/create" method="POST">'
                markup += '<p>'
                markup += '<label for="comment">Comment</label><br />'
                markup += '<textarea name="comment" rows="3" cols="50"></textarea><br />'
                markup += '<input type="submit" value="Comment" class="comment-form-submit"/>'
                markup += '</p>'
                markup += '<input type="hidden" name="post_id" value="' + str(post_id) + '"/>'
                markup += '<input type="hidden" name="user_id" value="' + self._session._user_id + '"/>'
                markup += '</form>'
                                                                              
            #check permissions and add delete, comment, and edit links here
            
            # markup += '</div>'

            markup += '<hr />'

        markup += '</div>'
        
        return markup
