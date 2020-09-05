#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 10:56:24 2019

@author: sungminkim
"""


"""

OPEN API(Application Programming Interface)
: 니가 필요한 정보들을 파라미터로 서버에 전달하면 open해 주는거다

Inter+face(면) = 너가 보이는 면과 내가 보이는 면이 만나는 지점 = 면면 간에
between

1. XML(대세) - Extended Markup Language -> <year>이런거</year>
2. JSON(대세)
3. CSV
4. TXT

Client <-> Server

예제)
https://hisnet.handong.edu/myboard/read.php?id=18337&Page=1&Board=B0029 -> read.php뒤에는 파라미터임 '&'로 구분
http://openapi.seoul.go.kr:8088/48437379626b736d3930624c736874/xml/octastatapi419/1/10/ -> 여기도 파라미터가 '/' 로 구분됨 


반대로 Closed API도 있다. 아무나 접근하지 못하게. OPEN API도 아무나 접근하지 못하게 인증키를 발급받은 사람에게만 접근허용.


"""

import pandas as pd
from bs4 import BeautifulSoup
import requests

url = 'http://openapi.seoul.go.kr:8088/4a4a5657506b676337375843707562/xml/octastatapi419/1/26/'
req = requests.get(url)
html = req.text
soup = BeautifulSoup(html, 'html.parser')

#print(html)
#print(soup)



jachigu = soup.find_all('jachigu')
#print(jachigu[0].text)
jachigu_list = []
for i in range(len(jachigu)):
    jachigu_list.append(jachigu[i].text)
    
    
sedae = soup.find_all('sedae')
#print(sedae[0].text)
sedae_list = []
for i in range(len(sedae)):
    sedae_list.append(sedae[i].text)
    


sedaeingu = soup.find_all('sedaedangingu')
sedaeingu_list = []
for i in range(len(sedaeingu)):
    sedaeingu_list.append(sedaeingu[i].text)
    

n_65seisang = soup.find_all('n_65seisanggoryeongja')
n_65seisang_list = []
for i in range(len(n_65seisang)):
    n_65seisang_list.append(n_65seisang[i].text)
    
    
Result = {} 
Result['자치구'] = jachigu_list
Result['세대수'] = sedae_list
Result['세대당 인구'] = sedaeingu_list
Result['65세이상 고령'] = n_65seisang_list

df = pd.DataFrame(Result)

df.drop([0],inplace = True) 

