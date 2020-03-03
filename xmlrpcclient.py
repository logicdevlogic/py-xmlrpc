#!/usr/bin/env python
# coding=utf-8


import xmlrpclib

server = xmlrpclib.ServerProxy("http://localhost:8088/test")

print server.add(2, 3)

