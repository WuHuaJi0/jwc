__author__ = 'zjhz'
import requests
from bs4 import BeautifulSoup

page = requests.get("http://www.baidu.com").text

bs = BeautifulSoup(page)


# print bs
p =  bs.find_all('a')

# sibling_soup.b.next_sibling
# <c>text2</c>

# sibling_soup.c.previous_sibling
# <b>text1</b>

print p[2]



