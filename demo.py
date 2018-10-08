#!/bin/env python
import urllib
import urllib2

#values = {"username":"","password":""}
values = {}
values["username"] = "18986108575"
values["password"] = "@dQQ1365710661"
data = urllib.urlencode(values)
#url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
url = "http://passport.csdn.net/account/login"
geturl = url + "?" + data
request = urllib2.Request(geturl)
response = urllib2.urlopen(request)
print response.read()
