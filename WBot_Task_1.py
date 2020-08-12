
# coding: utf-8

# # Task 1 - Getting to Philosophy

# In[15]:


# Import libraries necessary for this project
import urllib.request
import time


# In[ ]:


opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Chrome/35.0.1916.47')]

newURL= input('please Enter The URL ')

#Finds the first link/title (broken when it has a country)
def getNextURL(newURL): 
    infile = opener.open(newURL)
    page = infile.read().decode('utf-8')
    mainP = page[page.find('<p>'):page.find('<p>')+500] #Find the first <p> tag for the main body
    newPage = mainP[mainP.find('<a href="/wiki/')+15:mainP.find('"',mainP.find('<a href="/wiki/')+15)] #Find the first href for the link
    return newPage

newPage = getNextURL(newURL)


if newPage == 'Philosophy':
    print("your input page was the Philosophy page!")
else:
    print("Our Begining on the " + newPage + " page.")
    while newPage !='Philosophy':
        #Creates the next link to go to based upon the first link
        newURL = 'http://en.wikipedia.org/w/index.php?title=' + newPage 
        newPage = getNextURL(newURL)
        print ('Now opening the ' + newPage + ' page.')
        #Wait 0.5 second to avoid heavy load on Wikipedia
        time.sleep(0.5)

