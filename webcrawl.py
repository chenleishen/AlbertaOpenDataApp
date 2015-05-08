import urlparse
import urllib
import sqlite3
from bs4 import BeautifulSoup
import re

def findCSV(soup):
	distribution = soup.find("div", {"class" : "fieldgroup group-ds-distribution"})
	if (distribution != None):
		for tag in distribution.findAll('a', href=True):
			tag['href'] = urlparse.urljoin(url,tag['href'])
			if re.search("\.csv$", tag['href']):
				#print tag['href']
				break

rootPage = "http://data.alberta.ca/data"
urls = [rootPage]
visited = [rootPage]

while len(urls) > 0:
	url = urls.pop(0)
	try:
		htmltext = urllib.urlopen(url).read()
	except:
		print url

	soup = BeautifulSoup(htmltext)
	findCSV(soup)

	for tag in soup.findAll('a', href=True):
		tag['href'] = urlparse.urljoin(rootPage, tag['href'])
		if rootPage in tag['href'] and tag['href'] not in visited:
			urls.append(tag['href'])
			visited.append(tag['href'])

#print visited

