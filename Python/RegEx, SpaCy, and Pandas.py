#q1
import re
example = "There are a few 080-7365-6462 nkjahahsf 090-1234-1234 dsfkhw dk 03-7856-4578 fdsfs 0135-4355467-25656 make sure to check that your reges does not think all numeric sequences are phone numbers"
pattern = r"(?<!\d)(03-\d{4}-\d{4}|0[89]0-\d{4}-\d{4}(?!\d))"
result = re.findall(pattern, example)
print(result)

#q2
import spacy
from urllib import request
from collections import Counter
url = "https://www.gutenberg.org/cache/epub/1513/pg1513.txt"
response = request.urlopen(url)
raw = response.read().decode('utf8')

nlp = spacy.load("en_core_web_sm")
doc = nlp(raw)
common_entities =[]

for x in doc.ents:
    common_entities.append((x.text, x.label_))

entity_counts = Counter(common_entities)
most_common_entity = entity_counts.most_common(3)

for x, y in most_common_entity:
    print(x, y)

#q3
import pandas as pd
import random
first = pd.read_csv("https://raw.githubusercontent.com/hadley/data-baby-names/master/baby-names.csv")
last = pd.read_csv("https://raw.githubusercontent.com/fivethirtyeight/data/master/most-common-name/surnames.csv")
lastlist = last.name.tolist()
fnamelist = first.name.tolist()

#print(f"{fnamelist} {lastlist}")

def name():
    firstname = random.choice(fnamelist)
    lastname = random.choice(lastlist)

    return f"{firstname} {lastname}"

result = name()
print(result)