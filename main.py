#!/usr/bin/env python

import requests
from urllib2 import urlopen
from bs4 import BeautifulSoup

fb_user_name = raw_input("Enter your facebook username here: ")
fb_url = "http://graph.facebook.com/" + fb_user_name #to obtain specific username information
info = urlopen(fb_url).read()

#since we already know the JSON structure
#we can predict the fields and make the 
#information we obtained more presentable
#and easier to handle in the future.

#separates the json fields provided
separated = info.split(",") 
for i in separated:
	print i


###############################
######### TWITTER #############
###############################

tw_user_name = raw_input("Enter your twitter username here: ")
twitter_url = requests.get("http://twitter.com/" + tw_user_name)
twitter_html = BeautifulSoup(twitter_url.content)
print twitter_html



	