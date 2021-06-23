#!/usr/bin/env python

import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
        self.response.write('Hello, World3!')
=======


 

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)