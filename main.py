#!/usr/bin/env python

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
<<<<<<< HEAD
        self.response.write('Hello, World3!')
=======
        self.response.write('Hello, World!')
>>>>>>> parent of bb0add7 (4)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)