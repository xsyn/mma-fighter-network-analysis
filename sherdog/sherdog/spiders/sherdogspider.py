from scrapy import log, Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from sherdog.items import FightItem, AttrItem, FighterItem
import datetime as dt
import re

class SherdogSpider(CrawlSpider):
    name = "sherdog"
    allowed_domains = ["sherdog.com"]
    start_urls = ["http://www.sherdog.com/fighter/Mauricio-Rua-5707"]

    def my_process_value(value):
        m = re.search("http://m\.sherdog*", value)
        if m:
            return value.replace("http://m","http://www")
        else:
            return value

    rules = (
    Rule(SgmlLinkExtractor(allow = (r'/fighter/[a-zA-Z]+\-[a-zA-Z]+\-[0-9]+', ),process_value = my_process_value ),
         callback = "parse_item", follow = True),
         )

    def parse_item(self, response):
        # -- collect all table tags that has all the data
        hxs = Selector(response)
        tabs_odd = hxs.select("//tr[@class='odd']")
        tabs_even = hxs.select("//tr[@class='even']")
        tabs = [0] * (len(tabs_odd) + len(tabs_even))
        tabs[0::2] = tabs_odd
        tabs[1::2] = tabs_even

        # -- collect all fights

        Fights = {}
        i = 1
        for tab in reversed(tabs):
            FI = FightItem()
            FI["Verdict"] = tab.xpath(".//span/text()")[0].extract()
            FI["Opponent"] = tab.xpath(".//a[@href]/text()")[0].extract()
            FI["Event"] = tab.xpath(".//a[@href]//text()")[1].extract()
            FI["Date"] = dt.datetime.strptime(tab.xpath(".//span[@class='sub_line']/text()")[0].extract(), "%b / %d / %Y")
            FI["Method"] = tab.xpath(".//td/text()")[0].extract()
            FI["Round"] = int(tab.xpath(".//td/text()")[1].extract())
            if tab.xpath(".//td/text()")[2].extract() != "N/A":
                if re.search(";", tab.xpath(".//td/text()")[2].extract()):
                    FI["Time"] = sum(int(x) * 60 **k for k, x in enumerate(reversed(tab.xpath(".//td/text()")[2].extract().split(";"))))
                else:
                    FI["Time"] = sum(int(x) * 60 **k for k, x in enumerate(reversed(tab.xpath(".//td/text()")[2].extract().split(":"))))
            else:
                FI["Time"] = 0
            Fights["Fight" + str(i)] = dict(FI)
            i += 1

        # -- Bio of each fighter
        bio = hxs.xpath("//div[@class='bio']")
        AI = AttrItem()
        AI["Name"] = hxs.xpath(".//span[@class='fn']/text()")[0].extract()
        if bio.xpath(".//span[@itemprop='birthDate']/text()")[0].extract() != "N/A":
            AI["Birthday"] = dt.datetime.strptime(bio.xpath(".//span[@itemprop='birthDate']/text()")[0].extract(), "%Y-%m-%d")
        else:
             AI["Birthday"] = "Unknown"
        AI["Weight"] = int(bio.xpath(".//span[@class='item weight']//strong/text()").extract()[0].split()[0])
        AI["Height"] = sum(int(x) * 12 ** k for k, x in enumerate(reversed(bio.xpath(".//span[@class='item height']/strong/text()").extract()[0].split("\"")[0].split("\'"))))
        AI["Class"] = bio.xpath(".//strong[@class='title']/text()").extract()[0]
        if bio.xpath(".//strong[@itemprop='nationality']/text()").extract():
            AI["Country"] = bio.xpath(".//strong[@itemprop='nationality']/text()").extract()[0]

        # -- a nested dict
        Fighter = FighterItem()
        Fighter["Fights"] = dict(Fights)
        Fighter["Bio"] = dict(AI)

        log.msg('Currently getting ' + AI["Name"], level = log.WARNING)

        return Fighter
