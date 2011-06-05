#!/usr/bin/env python
"""
Resgen server frontend. Used to locally serve the webpage.
"""

import sys
sys.path.append("./webpy/")

import web

urls = (
        '/', 'index'
        )

class index:
    def GET(self):
        raise web.redirect("static/resgen_web.html")

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.internalerror = web.debugerror
    app.run()
