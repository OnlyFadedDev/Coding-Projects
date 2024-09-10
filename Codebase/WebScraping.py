import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
soupObject = BeautifulSoup(res.text, 'html.parser')
links = soupObject.select('.titleline')
votes = soupObject.select('.score')




