#!/usr/bin/python
#coding:utf-8
# test_db.py

__author = 'HSING LI'

from models import User, Blog, Comment

from transwarp import db

db.create_engine(user='root', password='root.org', database='blog', host='192.168.204.201')

u = User(name='person', email='person@blog.com', password='12345678', image='about:blank')

u.insert()

print('new user id:', u.id)

u1 = User.find_first('where email=?', 'person@blog.com')
print('find user\'s name:', u1.name)

# u1.delete()
#
# u2 = User.find_first('where email=？', 'person@blog.com')
# print('find user:', u2)