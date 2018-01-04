import urllib
import urllib2
import socket

__author__ = 'Yan'


STUID = 'xxx'
STUPASS = 'xxx'


def getv6ip():
    if socket.has_ipv6:
        addrinfos = socket.getaddrinfo(socket.gethostname(), 80, 0, 0, socket.IPPROTO_TCP)
        for addrinfo in addrinfos:
            if addrinfo[4][0].startswith('2001'):
                return addrinfo[4][0]


url = 'http://202.204.48.82/'


def main():
    getv6ip()
    data = {'DDDDD': STUID, 'upass': STUPASS, '0MKKey': '123456789', 'v6ip': getv6ip()}
    request = urllib2.Request(url, urllib.urlencode(data))
    response = urllib2.urlopen(request)
    print response.getcode()

if __name__ == '__main__':
    main()