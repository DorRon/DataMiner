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
print twitter_html.prettify() #makes html cleaner and more readable in the terminal
#dwindle down html to parse, since information we're looking for is inside specific div tags
twitter_bio_div = twitter_html.find_all("p", {"class": "ProfileHeaderCard-bio u-dir"}) 
twitter_place_div = twitter_html.find_all("div", {"class": "ProfileHeaderCard-location"})
twitter_url_div = twitter_html.find_all("div", {"class": "ProfileHeaderCard-url "})
twitter_join_div = twitter_html.find_all("div", {"class": "ProfileHeaderCard-joinDate"})
print twitter_bio_div, twitter_place_div, twitter_url_div, twitter_join_div


	





	