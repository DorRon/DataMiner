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



website('mikachoow21')