import os, re
from bs4 import BeautifulSoup
import datetime as dt

# sample
os.system("curl -O http://www.sherdog.com/fighter/Mauricio-Rua-5707")

soup = BeautifulSoup(open("Mauricio-Rua-5707").read())

# empty dictionary for each fighter
# will contain all fights and attributes
fighter = {}

# each past fight
tabs = soup.find_all("tr", class_ = re.compile("(even|odd)"))

for i in range(len(tabs)):
    fight = {}
    # fighter-
    tds = tabs[i].find_all("td")
    for j in range(len(tabs) - 1, 0, -1):
        fight["Verdict"] = tds[0].string
        fight["Opponent"] = tds[1].string
        fight["Event"] = tds[2].find("a").string
        fight["Date"] = dt.datetime.strptime(tds[2].find("span", class_ = "sub_line").string, "%b / %d / %Y")
        fight["Method"] = [k for k in tds[3].stripped_strings][0]
        fight["Round"] = int(tds[4].string)
        fight["Time"] = sum(int(x) * 60 ** k for k, x in enumerate(reversed(tds[5].string.split(":"))))
        pass
    fighter['Fight ' + str(i)] = fight
    pass

# background
bio = soup.find("div", class_ = "bio")

attr = {}

attr["Birthday"] = dt.datetime.strptime(bio.find("span", itemprop = "birthDate").string, "%Y-%m-%d")
attr["Weight"] = int(bio.find("span", class_ = "item weight").strong.string.split()[0])
attr["Height"] = sum(int(x) * 12 ** k for k, x in enumerate(reversed(bio.find("span", class_ = "item height").strong.string.split("\"")[0].split("\'"))))
attr["Class"] = bio.find("strong", class_ = "title").string
attr["Country"] = bio.find("strong", itemprop = "nationality").string

fighter["Bio"] = attr

##
