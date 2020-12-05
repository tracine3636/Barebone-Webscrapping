import requests #pip3 install requests
import bs4 #beautifulsoup

res = requests.get('https://learncodeonline.in')
type(res) #this records the data from the following website

#then type the following
res.text

