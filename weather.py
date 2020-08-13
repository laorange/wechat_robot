from bs4 import BeautifulSoup as bs
import re
import requests
url='http://tianqi.2345.com/dongli1d/60140.htm'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'}
wb_data=requests.get(url,headers=headers)
soup=bs(wb_data.text,'lxml')
temp=soup.find_all('div',class_='real-mess')
temp=str(list(temp)[0])
pattern = re.compile(r'<[^>]+>',re.S)
temp=pattern.sub('',temp)
temp=temp.split()
print(temp)
print(temp[5]+','+temp[6]+','+temp[7]+temp[8])
