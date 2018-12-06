
# most basic structure to grab
# html code 

# URLLIB
# generic, works on all python
# can read HTML, image files, other stuff
from urllib.request import urlopen
html = urlopen('http://pythonscraping.com/pages/page1.html')
print(html.read())
