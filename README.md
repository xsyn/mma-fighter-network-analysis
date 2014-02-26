# MMA Fighter Social Network Analysis

## Before

From

    if rawdata.startswith("<!", i):

to

    if rawdata.startswith("<!DOCTYPE", i):

in line 156 in the file:

    /usr/local/Cellar/python/2.7.5/Frameworks/Python.framework/Versions/2.7/lib/python2.7/sgmllib.py

Link: https://groups.google.com/forum/#!topic/scrapy-users/S-QfwhPpDtk

Scrapy version 0.18.3 and sgmllib.

## Scraping Data

### BeautifulSoup

I can scrape for individual fighter data pretty easily with
[BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/). Run
```parse_BeautifulSoup.py``` to grab fight history of
[Mauricio "Shogun" Rua](http://www.sherdog.com/fighter/Mauricio-Rua-5707)
into a dictionary.

### BaseSpider w/ Scrapy

Same deal as above except now uses [Scrapy](http://scrapy.org/). To
run the code, first ```cd``` into the ```sherdog/sherdog``` directory
and run:

    scrapy crawl shogun -o ../data/items.json -t json

To debug, run:

    scrapy shell http://www.sherdog.com/fighter/Mauricio-Rua-5707

### CrawlSpider w/ Scrapy to scrape the whole fighter database

(CrawlSpider not ready!)

    scrapy crawl sherdog -o ../data/results.json -t json

## Network Analysis

