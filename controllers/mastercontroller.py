#!/user/bin/env python

class MasterController:

    def markup(self, posts):
        #path = ('views/', args['class'], '/', args['method'], '.html')
        #markup = open(path, "r").read()
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
            markup += '<hr />'
                        
        return markup
