import requests
import re
import bs4
from bs4 import BeautifulSoup

response = requests.get('http://xueshu.baidu.com/u/citation?&callback=&sign=90a979f2e00fc66fa5b6003150dec2b5&diversion=6719295872988872705&url=http%3A%2F%2Fcdmd.cnki.com.cn%2FArticle%2FCDMD-80000-1016210106.htm&allversion=%5B%22http%3A%5C%2F%5C%2Fcdmd.cnki.com.cn%5C%2FArticle%5C%2FCDMD-80000-1016210106.htm%22%2C%22http%3A%5C%2F%5C%2Fwww.ixueshu.com%5C%2Fapi%5C%2Fsearch%5C%2Finfo%5C%2Fcc89624feb8e36ab5bcf200c2320ef7c318947a18e7f9386.html%22%5D&paperid=b5a4e69963ea819669fe9d8651136fec&t=cite&_=')
print(response.encoding)
print(response.text.encode('utf-8').decode("unicode_escape"))