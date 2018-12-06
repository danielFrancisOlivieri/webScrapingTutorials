# dealing with HTML

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://en.wikipedia.org/wiki/Stephen_Colbert')
bs = BeautifulSoup(html.read(), 'html.parser')

paragraphList = bs.body.find_all('b') # finds all bold tags

print(paragraphList[0].get_text())

# prints full list 
for i in paragraphList:
    print(i.get_text())

# navigating the tree 

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')
# prints a whole lot 
for child in bs.find('table',{'id':'giftList'}).children:
    print(child)

# descedents() is different from children()

for sibling in bs.find('table', {'id':'giftList'}).tr.next_siblings:
    print(sibling)

# be as specific as possible and use tags

# lamba expressions can be helpful