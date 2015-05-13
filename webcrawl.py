import urlparse
import urllib
import sqlite3
from bs4 import BeautifulSoup
import re

def Excel2CSV(ExcelFile, SheetName, CSVFile):
     import xlrd
     import csv
     workbook = xlrd.open_workbook(ExcelFile)
     worksheet = workbook.sheet_by_name(SheetName)
     csvfile = open(CSVFile, 'wb')
     wr = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

     for rownum in xrange(worksheet.nrows):
         wr.writerow(
             list(x.encode('utf-8') if type(x) == type(u'') else x
                  for x in worksheet.row_values(rownum)))

     csvfile.close()

def findCSV(soup):
	distribution = soup.find("div", {"class" : "fieldgroup group-ds-distribution"})
	#fileType = soup.find("td", {"class" : "distribution-format"})
	if (distribution != None):
		for tag in distribution.findAll('a', href=True):
			tag['href'] = urlparse.urljoin(url,tag['href'])
			if re.search("\.csv$", tag['href']):
				print "csv files: " + tag['href']
				#print fileType
				break
			elif re.search("\.xlsx", tag['href']):
				print "Excel Spreadsheets: " + tag['href']
				#print fileType
				break
			elif re.search("\.xls", tag['href']):
				print "Excel Spreadsheets: " + tag['href']
				#print fileType
				break 
			else:
				print "Other formats: " + tag['href']
				#print fileType
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

