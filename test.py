import requests
import bs4
import re
from bs4 import BeautifulSoup
#测试
#测试1
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
# reponse = requests.get('http://xueshu.baidu.com/s?wd=paperuri%3A%28aaaae129524ff45071f7ee0970d47e00%29&filter=sc_long_sign&sc_ks_para=q%3D%E5%93%A5%E5%BE%B7%E5%B0%94%E3%80%81%E8%89%BE%E8%88%8D%E5%B0%94%E3%80%81%E5%B7%B4%E8%B5%AB%20%3A%20%E9%9B%86%E5%BC%82%E7%92%A7%E4%B9%8B%E5%A4%A7%E6%88%90&sc_us=6551179971565419067&tn=SE_baiduxueshu_c1gjeupa&ie=utf-8&sc_as_para=sc_lib%3A')
# soup = BeautifulSoup(reponse.text,'html.parser')
# print(soup.find_all('noscript')[0].find(attrs={'http-equiv':'refresh'})['content'])
# str = soup.find_all('noscript')[0].find(attrs={'http-equiv':'refresh'})['content']
# response = requests.get(str.split('=',1)[1],headers=header)
# print(response.text)
data = {'dbId':'cb_beref_default','articleKeyword': '机器与语言;','authorKeyword': '徐愚;','orderBy': 'relevant','operate': 'search'}
response = requests.get('http://xueshu.baidu.com/s?wd=哥德尔、艾舍尔、巴赫——集异璧之大成+author(侯世达)&ie=utf-8&tn=SE_baiduxueshu_c1gjeupa&sc_f_para=sc_tasktype\{firstAdvancedSearch\}&sc_from=&sc_as_para=sc_lib:')
print(response.status_code)
print(response.text)
soup = BeautifulSoup(response.text,'html.parser')
cite_tag1 = soup.find_all('div',id='1')[0].find_all('i',attrs={'class':'reqdata'})[0]
cite_tag2 = soup.find_all('div',id='1')[0].find_all('i',attrs={'class':'reqdata'})[0]
url = cite_tag1.get('url')
urlmd = cite_tag1.get('urlmd')
sign = cite_tag1.get('longsign')
diversion = cite_tag1.get('diversion')
all_version = cite_tag1.get('allversion')
data_sign = cite_tag2.get('data-sign')
print(url,sign)
response = requests.get('http://xueshu.baidu.com/u/citation?&callback=&sign=%s&diversion=%s&url=%s&allversion=%s&paperid=%s&t=cite&_=' % (data_sign,diversion,url,all_version,sign))
print(response.encoding)
result = response.text.encode('utf-8').decode("unicode_escape")
print(result)
result_find = re.findall(r'"sc_GBT7714":"(.*?)"',result)
print(result_find)
