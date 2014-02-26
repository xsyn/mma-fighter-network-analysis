## check if json file is correct
## first do:
##   scrapy crawl sherdog -o data/aho.json -t json
## then grab aho.json line by line (delete the square brackets first)

import json

d = []
with open("data/aho.json") as f:
    for line in f:
        if line[(len(line)-2):] == ",\n":
            line = line[:(len(line)-2)]
            pass
        d.append(line)

d[0] = d[0][1:]

d_ = [json.loads(i) for i in d[2:5]]
