#!/usr/bin/env python
# coding=utf-8

from SimpleXMLRPCServer import MultiPathXMLRPCServer

from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
from SimpleXMLRPCServer import SimpleXMLRPCDispatcher

from concurrent.futures import ThreadPoolExecutor

from SocketServer import ThreadingMixIn

class PoolMixIn(ThreadingMixIn):
    def process_request(self, request, client_address):
        self.pool.submit(self.process_request_thread, request, client_address)

class MultiPathRequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ()

class BMultiPathXMLRPCServer(PoolMixIn, MultiPathXMLRPCServer):
    pool = ThreadPoolExecutor(max_workers=100)

class calculate:
    def add(self, x, y):
        import time
        time.sleep(10)

        return x + y

    def multiply(self, x, y):
        return x * y

    def subtract(self, x, y):
        return abs(x-y)

    def divide(self, x, y):
        return x/y


server = BMultiPathXMLRPCServer(("localhost", 8088), requestHandler=MultiPathRequestHandler)

obj = calculate()
d = server.add_dispatcher("/test", SimpleXMLRPCDispatcher())
d.register_instance(obj)

print "Listening on port 8088"
server.serve_forever()


