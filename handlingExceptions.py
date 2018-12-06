# handling exceptions 

# 2 main things to go wrong
# 1. page is not found or error in retrieving
# 2. server not found 

from urllib.request import urlopen
from urllib.error import HTTPError

# for page not being found: 

try:
    html = urlopen('http://www.pythonscraping.com/pages/page1.html')

except HTTPError as e:
    print(e)
    # return null, break, or do some other "Plan B"
except URLError as e: 
    print('The server could not be found!')
else:
    print('It Worked!')   
    # program continues. Note: If you return or break in the  
    # exception catch, you do not need to use the "else" statement


# checking for errors in the html itself

    try: 
        badContent = bs.nonExistingTag.anotherTag
    except AttributeError as e:
        print("Tag not found")
    else:
        if badContent == None:
            print("Tag not found")
        else:
            print(badContent)
