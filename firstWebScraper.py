# first web crawler

from urllib.request import urlopen
from bs4 import BeautifulSoup 
import datetime
import random
import re

random.seed(datetime.datetime.now()) # produces a random seed 

# precon: internet connection 
# postcon: returns a bs object of all links in the bodyContent div of the wiki page
def getLinks(articleUrl):
    html = urlopen('http://en.wikipedia.org{}'.format(articleUrl)) # opens whichever wikipedia page you hand it
    bs = BeautifulSoup(html, 'html.parser') # parses that document into a bs object
    # first function finds the main body div, 
    # second uses a regex to find all appropriate links 
    return bs.find('div', {'id': 'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$')) 

# this is the end of the url for our actor
links = getLinks('/wiki/Kevin_Bacon')

count = 0

while len(links) > 0:
    newArticle = links[random.randint(0, len(links) -1)].attrs['href']
    print('****************'+ str(count) +'***************')
    print(newArticle)
    links = getLinks(newArticle)
    count+= 1
    if count > 17:
        break
