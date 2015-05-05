import urlparse
import urllib
import sqlite3
from bs4 import BeautifulSoup
import re


url = "http://data.alberta.ca/data"
#url = "http://data.alberta.ca/data/agricultural-processing-industry-directory"

urls = [url] #stack of urls to scrape
visited = [url] #historic record of urls

while len(urls) > 0:
	url = urls.pop(0)
	try:
		htmltext = urllib.urlopen(url).read()
	except:
		print url

	soup = BeautifulSoup(htmltext)

	for tag in soup.findAll('a', href=True):
		tag['href'] = urlparse.urljoin(url,tag['href'])
		if re.search("\.csv$", tag['href']):
			print tag['href']
			break
		if url in tag['href'] and tag['href'] not in visited:
			urls.append(tag['href'])
			visited.append(tag['href'])

#print visited