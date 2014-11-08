#!/usr/bin/env python

from urllib2 import urlopen
import json

user_name = raw_input("Enter your facebook username here: ")
url = "http://graph.facebook.com/" + user_name #to obtain specific username information
info = urlopen(url).read()

#since we already know the JSON structure
#we can predict the fields and make the 
#information we obtained more presentable
#and easier to handle in the future.

#separates the json fields provided
separated = info.split(",") 
for i in separated:
	print i


	