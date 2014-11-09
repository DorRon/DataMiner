from bs4 import BeautifulSoup
import requests

def email(github_username):
	github_url = "http://github.com/" + github_username
	github_html = requests.get(github_url)
	soup = BeautifulSoup(github_html.content)

	email = soup.find_all('a',{'class':'email'})
	email = str(email[0])

	index = email.find('>') + 1

	email = email[index:]

	index = email.find("<") 
	email = email[:index]

	return email

def name(github_username):
	github_url = "http://github.com/" + github_username
	github_html = requests.get(github_url)
	soup = BeautifulSoup(github_html.content)

	name = str(soup.title)
	
	index = name.find("(") + 1

	name = name[index:]
	
	index = name.find(")")

	name = name[:index]
	return name

def website(github_username):
	github_url = "http://github.com/" + github_username
	github_html = requests.get(github_url)
	soup = BeautifulSoup(github_html.content)

	website  = str(soup.find_all('a', {'class': 'url'})[0])

	index = website.find('>') + 1

	website = website[index:]

	index = website.find("<") 
	website = website[:index]

	return website

def date_joined(github_username):
	github_url = "http://github.com/" + github_username
	github_html = requests.get(github_url)
	soup = BeautifulSoup(github_html.content)

	date_joined = str(soup.find_all('time', {'class':'join-date'})[0])

	index = date_joined.find('>') + 1

	date_joined = date_joined[index:]

	index = date_joined.find("<") 
	date_joined = date_joined[:index]

	return date_joined

def location(github_username):
	github_url = "http://github.com/" + github_username
	github_html = requests.get(github_url)
	soup = BeautifulSoup(github_html.content)

	location = str(soup.find_all('li', {'itemprop':'homeLocation'})[0])

	index = location.find('</span') + 7

	location = location[index:]

	index = location.find("<") 
	location = location[:index]

	return location









