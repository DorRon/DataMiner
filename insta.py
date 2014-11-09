from bs4 import BeautifulSoup
import requests


def getAll(user):

	r=requests.get("http://iconosquare.com/"+user)

	soup=BeautifulSoup(r.content)

	s=soup.find_all("meta",{"itemprop":"image"})[0].get("content")

	return s