

import requests
from bs4 import BeautifulSoup

url = "http://www.tweakers.net"
r = requests.get(url)

soup = BeautifulSoup(r.content)

links = soup.find_all("a")

for link in links:
    print "<a href='%s'>%s</a>" %(link.get("href), link.text)
