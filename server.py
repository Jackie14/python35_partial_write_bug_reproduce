#!/usr/bin/env python3
# SPDX-License-Identifier: BSD-3-Clause

import time
import os
import sys
import subprocess

server_ip = ''

def http_server():
    from http.server import HTTPServer, SimpleHTTPRequestHandler
    httpd = HTTPServer((server_ip, 0), SimpleHTTPRequestHandler)
    print(httpd.server_address)
    httpd.serve_forever()


def create_http_server_thread():
    import threading
    thread = threading.Thread(target=http_server, daemon=True)
    thread.start()
    time.sleep(2) # Wait thread start and set the port.

def create_http_server_process():
    from multiprocessing import Process
    process = Process(target=http_server)
    process.daemon = True
    process.start()
    time.sleep(2) # Wait process start and set the port.

server_ip = sys.argv[1]
print("Got server ip: {}".format(server_ip))
print("Create HTTP server on:")
create_http_server_thread()
# If switch to use sub process to host http server, then the download failure issue can be avoided
#create_http_server_process()
for i in range(1000000000):
   os.system('date > /dev/null') 
   # The more frequently we call os.system, the more frequently download failure happen
   time.sleep(0.1)