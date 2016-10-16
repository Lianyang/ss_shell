#!/usr/bin/env python
#-*-coding:utf-8-*-

from local import main
from HTMLParser import HTMLParser
from urllib import urlopen
import time
import signal
import sys

class Myhtmlparser(HTMLParser):
    def handle_data(self, data):


def get_password():
    online = 1
    while online:
        try:
            online = 0
            text = urlopen('http://www.ishadowsocks.com/').read()
        except Exception,e:
            print e
            online = 1
            time.sleep(1)
    parser = MyHTMLParser()
    parser.feed(text)
    password = parser.jp3pass
    print password
    return password

