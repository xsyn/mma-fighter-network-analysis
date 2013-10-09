# MMA Fighter Social Network Analysis

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

    scrapy crawl shogun -o ../../data/items.json -t json

### CrawlSpider w/ Scrapy to scrape the whole fighter database

(CrawlSpider not ready!)

    scrapy crawl sherdog -o ../../data/results.json -t json
	
## Network Analysis

