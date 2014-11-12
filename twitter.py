#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup

###############################
######### TWITTER #############
###############################
def getAll(tw_user_name):
	#tw_user_name = raw_input("Enter your twitter username here: ")
	twitter_url = requests.get("http://twitter.com/" + tw_user_name)
	twitter_html = BeautifulSoup(twitter_url.content) 
	#print twitter_html.prettify() #makes html cleaner and more readable in the terminal
	#dwindle down html to parse, since information we're looking for is inside specific div tags
	twitter_bio_div = twitter_html.find_all("p", {"class": "ProfileHeaderCard-bio u-dir"}) 
	twitter_place_div = twitter_html.find_all("div", {"class": "ProfileHeaderCard-location"})
	twitter_url_div = twitter_html.find_all("div", {"class": "ProfileHeaderCard-url "})
	twitter_join_div = twitter_html.find_all("span", {"class": "ProfileHeaderCard-joinDateText js-tooltip u-dir"})
	#print twitter_bio_div, twitter_place_div, twitter_url_div, twitter_join_div
	#convert divs to strings to make it easier to manipulate them
	#must do individually since str function only accepts 1 argument
	twitter_url_string = str(twitter_url_div)
	twitter_join = str(twitter_join_div)
	twitter_place = str(twitter_place_div)
	twitter_bio = str(twitter_bio_div)
	#make a list out of the strings for separation, then revert back to string with desired content
	place2 = twitter_place.split(">")
	place3 = place2[-3:-2]
	final_str = str(place3)
	twitter_user_place = final_str[2:-8] #only saves the city and state from location div (always be within that index)
	#print "\n"*10
	twitter_user_url = twitter_url_div[0].a.get("title")
	twitter_user_join = twitter_join_div[0].get("title")
	twitter_user_bio = twitter_bio_div[0].text	
	d={"URL":twitter_user_url, "JoinDate":twitter_user_join, "Location":twitter_user_place, "Bio":twitter_user_bio}
	return d
print getAll("mikachoow21")