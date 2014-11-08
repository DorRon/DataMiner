#!/usr/bin/env python

from urllib2 import urlopen
import json

user_name = raw_input("Enter your facebook username here: ")
url = "http://graph.facebook.com/" + user_name #to obtain specific username information
info = urlopen(url).read()
print info

