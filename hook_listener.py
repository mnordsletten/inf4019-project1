#!/usr/bin/env python

import web
import json

urls = ('/.*', 'hooks')

app = web.application(urls, globals())

class hooks:
    def handle_push(self,js):
        print "About to handle push event for repository " + js["repository"]["name"]
        print "Push done by " + js["user_email"]
        # this is where you add your code
        return

    def POST(self):
        data = web.data()
        print
        print 'DATA RECEIVED:'
        print data
        js = json.loads(data)
        print "Object kind: " + js["object_kind"]
        self.handle_push(js)
        print
        return 'OK'

        
        
if __name__ == '__main__':
    app.run()

