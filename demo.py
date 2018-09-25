#!/bin/env python

import urllib2

response = urllib2.urlopen("http://baidu.com")
print response.read()
