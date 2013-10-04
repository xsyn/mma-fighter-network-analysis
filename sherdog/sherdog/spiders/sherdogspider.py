from scrapy.spider 	import BaseSpider
from scrapy.selector import HtmlXPathSelector
from sherdog.items	import FightItem, AttrItem, FighterItem
from scrapy.http	import Request
import datetime as dt
import re

class SherdogSpider(BaseSpider):
    name = "sherdog"
    allowed_domains = ["sherdog.com"]
    start_urls = ["http://www.sherdog.com/fighter/Mauricio-Rua-5707"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        tabs = hxs.select("//tr[@class='even']")
        i = 1
        for tab in reversed(tabs):
            FI = FightItem()
            FI["Verdict"] = tab.select("./td")
            FI["Opponent"]
            FI["Event"]
            FI["Date"]
            FI["Method"]
            FI["Round"]
            FI["Time"]
            Fighter["Fight" + str(i)] = FI
            i += 1
        bio = hxs.select("//div[@class='bio']")
        AI = AttrItem()
        AI["Birthday"] = dt.datetime.strptime(bio.select(".//span[@itemprop='birthDate']/text()")[0].extract(), "%Y-%m-%d")
        AI["Weight"] = int(bio.select(".//span[@class='item weight']//strong/text()").extract()[0].split()[0])
        AI["Height"] = sum(int(x) * 12 ** k for k, x in enumerate(reversed(bio.select(".//span[@class='item height']/strong/text()").extract()[0].split("\"")[0].split("\'"))))
        AI["Class"] = bio.select(".//strong[@class='title']/text()").extract()[0]
        AI["Country"] = bio.select(".//strong[@itemprop='nationality']/text()").extract()[0]
        Fighter["Bio"] = AI
