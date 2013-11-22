#!/user/bin/env python

class MasterController:

    def markup(self):
        path = ('views/', args['class'], '/', args['method'], '.html')
        markup = open(path, "r").read()
        return markup
