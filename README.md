## This repo code is used to reproduce a bug of python3.5.

There is a bug in python3.5, which is already fixed from python3.6.
In case python3.5 is a must, we need to reproduce that bug(to make sure of it) and patch to fix.

## Python3.5 bug info
### Issue:
https://github.com/python/cpython/issues/70908

### Fix:
https://github.com/python/cpython/commit/34eeed42901666fce099947f93dfdfc05411f286#diff-c00d56a0c132ee4bdf79f55a4b43643cf314df1fe122c07c539e120c7ec98b5e


## Steps to reproduce:

0) In the diretory you want to start the server.py script, please prepare a file( >1MB) used for downloading.

        $ dd if=/dev/zero of=1MBfile.txt bs=1M count=1

1) Start a HTTP server, by python3.5

        $ python3.5 ./server.py 10.237.121.80
        Got server ip: 10.237.121.80
        Create HTTP server on:
        ('10.237.121.80', 43079)

2) Try to download a file (>1MB) from that HTTP server, on another host.
You will get download failure in some cases.
if you switch to use >=python3.6 to start the server.py, you will not get those download failure


        $ sh client.sh curl 10.237.121.80 43079 1MBfile.txt
        ...

        *   Trying 10.237.121.80...
        * TCP_NODELAY set
        * Connected to 10.237.121.80 (10.237.121.80) port 43079 (#0)
        > GET /1MBfile.txt HTTP/1.1
        > Host: 10.237.121.80:43079
        > User-Agent: curl/7.61.1
        > Accept: */*
        >
        * HTTP 1.0, assume close after body
        < HTTP/1.0 200 OK
        < Server: SimpleHTTP/0.6 Python/3.5.0
        < Date: Fri, 25 Oct 2024 12:19:17 GMT
        < Content-type: text/plain
        < Content-Length: 1048576
        < Last-Modified: Fri, 25 Oct 2024 11:51:29 GMT
        <
        { [8688 bytes data]
        * transfer closed with 10360 bytes remaining to read
        * Closing connection 0

        curl: (18) transfer closed with 10360 bytes remaining to read
        Error!!! Error!!!



        $ sh client.sh wget 10.237.121.80 43079 1MBfile.txt
        ...

        --2024-10-25 15:17:26--  http://10.237.121.80:43079/1MBfile.txt
        Connecting to 10.237.121.80:43079... connected.
        HTTP request sent, awaiting response... 200 OK
        Length: 1048576 (1.0M) [text/plain]
        Saving to: ‘1MBfile.txt.37’

        1MBfile.txt.37                                      99%[=============================================================================================================> ]   1018K  --.-KB/s    in 0.009s

        2024-10-25 15:17:26 (115 MB/s) - Connection closed at byte 1042296. Giving up.

        Error!!! Error!!!





