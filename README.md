Databases we have
-employment rate by cities towns 
-non employment rate 
-consumer index
-expenditures 
-education level etc etc.

Steps: 
-crawl website for url links
-find out what we can clean, etc by cities 
-think of list of meta data categories we will be going with
-get keywords, column/row tags, etc other meta data
-clean data: filters out relevant info only
-create catalog of datasets, add meta data to the dataset itself for our program to interact with 
-user interface for sorting data using metadata

To do for the crawler:
Chenlei and Andrew:
-figure out what metadata to put into database
-search for excel files, use python library to convert into csv
-figure how to access the rest of the csv files that are embedded in a redirect link
-figure what to do with shape files and json files
Jerry and Jerry:
-Once we scrape all the data we can decide what to do with it next (web app!)
(good start! :))

Crawler Documentation
Setup environment for the crawler on a Mac:
-Beautiful Soup
-Home brew (to download mysql, recommended but not required AKA have fun install mysql your way)
-MySQL Python
-xlrd module for python

To download beautifulsoup on mac:
go to http://www.crummy.com/software/BeautifulSoup/bs4/download/
download latest version
unzip it
go into the beautifulsoup folder via cmd
type “python setup.py”

To download Home brew
Just follow the instructions on Home Brew website
http://brew.sh/

To download Mysql below are the steps:
Install python
Type “brew install mysql” into cmd
Type “export PATH=$PATH:/usr/local/mysql/bin”
Type “pip install MySQL-Python”
Done

To install xlrd module:
Type “pip install xlrd”

Setup environment for a PC user:
-Python (Windows do not have python pre-installed)
-Pip (should come pre-installed with Python)
-Beautiful Soup
-Easy Install
-MySQL Python
 
Useful stuff for both:
Different methods to install python modules - http://docs.webfaction.com/software/python.html#installing-python-packages
Comparison between using pip vs. easy_install
http://stackoverflow.com/questions/3220404/why-use-pip-over-easy-install

Useful stuff for mac:
Homebrew setup - http://brew.sh/
Beautiful soup documentation - http://www.crummy.com/software/BeautifulSoup/bs4/doc/
How to install python - http://stackoverflow.com/questions/25459386/mac-os-x-environmenterror-mysql-config-not-found

Useful stuff for PC:
how to setup python on windows - http://www.anthonydebarros.com/2011/10/15/setting-up-python-in-windows-7/
http://www.stat.ucla.edu/~rosario/classes/07F/202a/python/
how to install pip on windows (it should come pre-installed with python, but if not) - 
http://stackoverflow.com/questions/21440230/install-mysql-python-windows
Install Beautiful Soup - http://stackoverflow.com/questions/12228102/how-to-install-beautiful-soup-4-with-python-2-7-on-windows

Excel to CSV
Function to convert excel files to csv files - http://stackoverflow.com/questions/26029095/python-convert-excel-to-csv
XLRD module documentation - https://secure.simplistix.co.uk/svn/xlrd/trunk/xlrd/doc/xlrd.html?p=4966
How to download csv - http://stackoverflow.com/questions/18037184/how-to-save-a-csv-to-a-local-directory-in-python



