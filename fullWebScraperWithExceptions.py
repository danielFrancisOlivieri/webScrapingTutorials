# full webscraper WITH exceptions

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title = bs.body.h1 # here is where to edit to change what it retrieves
    except AttributeError as e:
        return None
    return title

title = getTitle('https://en.wikipedia.org/wiki/Stephen_Colbert')
if title == None:
    print('Title could not be found')
else:
    print(title)