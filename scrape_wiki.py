from bs4 import BeautifulSoup as Soup
import urllib.request
import sqlite3
import codecs
import queue
import time
import re

pages_dir = "./wiki_pages/"
sql_file = './pages.db'
pages_table = 'pages'
links_table = 'links'

seed_page = "http://www.en.wikipedia.org/wiki/Toronto"
pages = queue.Queue()
pages.put(seed_page)

connection = sqlite3.connect(sql_file)
cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS " + pages_table + ";")
cursor.execute("CREATE TABLE IF NOT EXISTS " + pages_table +
               " (url varchar(40), location varchar(40) ); " )

cursor.execute("DROP TABLE IF EXISTS " + links_table + ";")
cursor.execute("CREATE TABLE IF NOT EXISTS " + links_table +
                " (from_url varchar(40), to_url varchar(40) ); ")

connection.commit()

def clean_text(text):
    return text

def is_wiki_link(url):
    if (re.match("^/wiki/", url)):
        if (not re.search("\..{2,5}$", url)):
            return True
    return False

i = 0

while i < 100:
#while not pages.empty():
    start_time = time.clock()
    
    current_page = pages.get()
    print(current_page)
     
    request = urllib.request.urlopen(current_page)
    page_html = request.read().decode("utf-8")
    page = Soup(page_html)
    
    page_name = page.title.string
    
    page_file = codecs.open(pages_dir + page_name,  'w', "utf-8")
    cursor.execute("INSERT INTO " +  pages_table 
                   + " values ('" + current_page + "', '" + page_name + "');")
    for paragraph in page.find_all("p"):
        paragraph = clean_text(paragraph.get_text())
        page_file.write(paragraph + "\n")

    page_file.close()
    
    for url in page.find_all("a"):
        url_text = url.get("href")

        if (url_text != None):
            if(is_wiki_link(url_text)):
                pages.put("http://en.wikipedia.org" + re.sub("$.*#", "", url_text))
                cursor.execute("INSERT INTO " + links_table
                               + " values ('" + current_page + "', '" + re.sub("$.*#", "", url_text)
                               + "');")

    connection.commit()

    sleep_time = time.clock() - start_time
    if(sleep_time < 1):
        time.sleep(1 - sleep_time)

    i += 1




