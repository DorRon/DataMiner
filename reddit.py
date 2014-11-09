from bs4 import BeautifulSoup
import requests

def link_karma(reddit_username):
	reddit_url = "http://reddit.com/user/" + reddit_username
	reddit_html = requests.get(reddit_url)
	soup = BeautifulSoup(reddit_html.content)

	link_karma = str(soup.find_all('span',{'class':'karma'})[0])

	index = link_karma.find('>') + 1

	link_karma = link_karma[index:]

	index = link_karma.find("<") 
	link_karma = link_karma[:index]

	print link_karma

def comment_karma(reddit_username):
	reddit_url = "http://reddit.com/user/" + reddit_username
	reddit_html = requests.get(reddit_url)
	soup = BeautifulSoup(reddit_html.content)

	comment_karma = str(soup.find_all('span',{'class':'comment-karma'})[0])

	index = comment_karma.find('>') + 1

	comment_karma = comment_karma[index:]

	index = comment_karma.find("<") 
	comment_karma = comment_karma[:index]

	print comment_karma
