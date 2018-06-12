# -*- coding: utf-8 -*-
# try something like
def index(): return dict(message="hello from blog.py")

def post():
    form = SQLFORM(db.blog).process()
    return locals()

def views():
    #this line selects rows in db by id in a descending order
    rows = db(db.blog).select(orderby=~db.blog.id)
    return locals()
