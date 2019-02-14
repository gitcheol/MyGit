#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
#
##CCTV 데이터 파악
#
#
CCTV_Seoul = pd.read_csv("cctv.csv",  encoding='utf-8')
##print(CCTV_Seoul.head()) #head() print top 5 rine
#print(CCTV_Seoul.columns)
##
CCTV_Seoul.rename(columns={CCTV_Seoul.columns[0] : '구별'}, inplace=True)
##print(CCTV_Seoul.columns)
##
Temp = CCTV_Seoul.sort_values(by='소계', ascending=True)
#print(Temp.head())
##
CCTV_Seoul['최근증가율'] = (CCTV_Seoul['2016년'] + CCTV_Seoul['2015년'] + CCTV_Seoul['2014년']) / CCTV_Seoul['2013년도 이전'] * 100
##
#Temp = CCTV_Seoul.sort_values(by='최근증가율', ascending=False)
#print(Temp.head())
#
#
##서울시 인구 데이터 파악
#
#pop_Seoul = pd.read_excel('Report.xls',  encoding='utf-8')
#print(pop_Seoul.head())
#print(pop_Seoul.columns)
#
pop_Seoul = pd.read_excel('Report.xls',  usecols = 'B,C,D,E',  encoding='utf-8')
#print(pop_Seoul.head())
#
pop_Seoul.rename(columns={pop_Seoul.columns[0] : '구별', pop_Seoul.columns[1] : '인구', pop_Seoul.columns[2] : '남', pop_Seoul.columns[3] : '여'}, inplace=True)
#print(pop_Seoul.head())
#
pop_Seoul.drop([0], inplace=True)
#print(pop_Seoul.head())
#
#print(pop_Seoul['구별'].unique())
#
pop_Seoul.sort_values(by='인구', ascending=False, inplace=True)
#print(pop_Seoul.head())
#
#pop_Seoul.sort_values(by='인구', ascending=True, inplace=True)
#print(pop_Seoul.head())
#
##CCTV 데이터와 인구 데이터 합치고 분석
#
data_result = pd.merge(CCTV_Seoul, pop_Seoul, on='구별')
#print(data_result.head())

del data_result['2013년도 이전']
del data_result['2014년']
del data_result['2015년']
del data_result['2016년']
#print(data_result.head())

data_result.set_index('구별', inplace=True)
#print(data_result.head())
#
#Temp = data_result.sort_values(by='소계', ascending=False)
#print(Temp.head())
#
#Temp = data_result.sort_values(by='인구', ascending=False)
#print(Temp.head())
#
##CCTV와 인구현황 그래프로 분석
#
##환경맞춤
import platform
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system... sorry~~~~')


#CCTV수 그래프
#plt.figure()
#data_result['소계'].plot(kind='barh', grid=True, figsize=(10,10))
#plt.show()

##CCTV수 정렬 그래프
#data_result['소계'].sort_values().plot(kind='barh', grid=True, figsize=(10,10))
#plt.show()
#
#인구당 CCTV 비율 그래프
#data_result['CCTV비율'] = data_result['소계'] / data_result['인구'] * 100
#
#data_result['CCTV비율'].sort_values().plot(kind='barh', 
#                                         grid=True, figsize=(10,10))
#plt.show()
##
##인구대비 CCTV 숫자 분포도
#plt.figure(figsize=(6,6))
#plt.scatter(data_result['인구'], data_result['소계'], s=50) #s is size of marking
#plt.xlabel('인구')
#plt.ylabel('CCTV')
#plt.grid()
#plt.show()
#
# draw polyfit (대표적 경향 표현)
import numpy as np
#
#fp1 = np.polyfit(data_result['인구'], data_result['소계'], 1)
#
#f1 = np.poly1d(fp1)
#fx = np.linspace(100000, 700000, 100)
#
#plt.figure(figsize=(10,10))
#plt.scatter(data_result['인구'], data_result['소계'], s=50)
#plt.plot(fx, f1(fx), ls='dashed', lw=3, color='g')
#plt.xlabel('인구')
#plt.ylabel('CCTV')
#plt.grid()
#plt.show()
#
# 경향에서 많이 벗어난 10개 지역 이름 표시
fp1 = np.polyfit(data_result['인구'], data_result['소계'], 1)

f1 = np.poly1d(fp1)
fx = np.linspace(100000, 700000, 100)

data_result['오차'] = np.abs(data_result['소계'] - f1(data_result['인구'])) #append error data_result  to data_result.

df_sort = data_result.sort_values(by='오차', ascending=False) #sorting 
print(df_sort.head())

plt.figure(figsize=(7,5))
plt.scatter(data_result['인구'], data_result['소계'], 
            c=data_result['오차'], s=50)
plt.plot(fx, f1(fx), ls='dashed', lw=3, color='g') #dashed : express line by dot

for n in range(3):
    plt.text(df_sort['인구'][n]*1.02, df_sort['소계'][n]*0.98, df_sort.index[n], fontsize=15)
    
plt.xlabel('인구')
plt.ylabel('CCTV')
plt.colorbar()
plt.grid()
plt.show()
