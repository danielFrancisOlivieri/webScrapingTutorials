
# using beautiful Soup
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page1.html')

# this line puts the html from the source into a beautifulSoup object
# first parameter is the text, the second specifies the parser 
# in most cases it's unimportant which parser you choose
# the lxml parser is better at understanding malformed html
# it can be downloaded easily
# html5lib is also a good parser 
# .read() is not necessary here
bs = BeautifulSoup(html.read(), 'lxml')



'''
These all produce the same output:
bs.html.body.h1
bs.body.h1
bs.html.h1
'''

print(bs.h1)