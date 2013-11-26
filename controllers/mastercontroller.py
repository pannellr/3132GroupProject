#!/user/bin/env python

class MasterController:

    def markup(self, posts):
        
        markup = ''
        markup += '<div id="wrap2">'
        markup += '<img border="0" src="gglogo.png" alt="gogeo logo" width="250" height="125">'
        markup += '<img border="0" src="banner.png" alt="banner" width="1000" height="125">'
        markup += '</div>'
        markup += '</br >'
        markup += '<div id="wrap">'
        markup += '<h3> Geo-Location </h3>'
        markup += '<div id="map">'
        markup += '</div>'
        markup += '</div>'

        markup += '<div id="wrap4">'
        
        
        while True:
            post = posts.fetch_row(1,1)
            if not post: break
            markup += '<div class="post-wrapper">'
            markup += '<span class="post-author">Author: '
            markup += str(post[0]['user_id'])
            markup += '</span>'
            markup += '<span class="post-location">'
            markup += 'lat: ' + str(post[0]['lat']) + ' lng: ' + str(post[0]['lng'])
            markup += '</span>'
            markup += '<div class="post-content">'
            markup += post[0]['post']
            markup += '</div>'
            markup += '<span class="post-date"><em>' + post[0]['created_at'].strftime('%m/%d/%Y') + '</em></span>'
            markup += '</div>'
            # add options here
            markup += '<hr />'


        # test session state here
        markup += '<form action="post/create" method="POST" class="post-form">'
        markup += '<p>'
        markup += '<label for="post">Post</label><br />'
        markup += '<textarea name="post" rows="5" cols="80"></textarea><br />'
        markup += '<input type="submit" value="Post" class="post-form-submit"/>'
        markup += '</p>'
        
        return markup
