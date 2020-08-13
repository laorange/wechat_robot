from bs4 import BeautifulSoup as bs
import re
import requests
url='http://tianqi.2345.com/dongli1d/60140.htm'
wb_data=requests.get(url)
soup=bs(wb_data.text,'lxml')
temp=soup.find_all('div',class_='real-mess')
temp=list(temp)[0]
pattern = re.compile(r'<[^>]+>',re.S)
temp=pattern.sub('',temp)
print(temp)
