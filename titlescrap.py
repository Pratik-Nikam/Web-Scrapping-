from urllib.request import urlopen
from bs4 import BeautifulSoup
url = "http://www.hubertiming.com/results/2017GPTR10K"
html = urlopen(url)
soup = BeautifulSoup(html, 'lxml')
type(soup)
bs4.BeautifulSoup
# Get the title
title = soup.title
print(title)
# Print out the text
text = soup.get_text()
#print(soup.text)
