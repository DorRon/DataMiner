from bs4 import BeautifulSoup
import requests
def getAll(reddit_username):
	L=[link_karma(reddit_username),comment_karma(reddit_username)]
	return L

def link_karma(reddit_username):
	reddit_url = "http://reddit.com/user/" + reddit_username
	reddit_html = requests.get(reddit_url)
	soup = BeautifulSoup(reddit_html.content)

	link_karma = str(soup.find_all('span',{'class':'karma'})[0])

	index = link_karma.find('>') + 1

	link_karma = link_karma[index:]

	index = link_karma.find("<") 
	link_karma = link_karma[:index]

	return link_karma

def comment_karma(reddit_username):
	reddit_url = "http://reddit.com/user/" + reddit_username
	reddit_html = requests.get(reddit_url)
	soup = BeautifulSoup(reddit_html.content)

	comment_karma = str(soup.find_all('span',{'class':'comment-karma'})[0])

	index = comment_karma.find('>') + 1

	comment_karma = comment_karma[index:]

	index = comment_karma.find("<") 
	comment_karma = comment_karma[:index]

	return comment_karma
