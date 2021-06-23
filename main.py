app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)


#!/usr/bin/env python

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello, World1!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)