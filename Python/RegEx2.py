# q4
import re
from urllib import request

url = "https://www.gutenberg.org/files/84/84-0.txt"
response = request.urlopen(url)
raw = response.read().decode('utf8')

p = re.compile(r"\w+\smonster\s\w+")
m = p.findall(raw)
print(m)

# q5

p = re.compile(r"\w{6,}")
m = p.findall(raw)
print(m)
