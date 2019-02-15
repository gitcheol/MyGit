#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Regression
#source from https://github.com/PinkWink/DataScience/blob/master/source_code/07.%20Time%20Series%20Data%20Handle.ipynb

import pandas as pd
import pandas_datareader.data as web
import numpy as np
import matplotlib.pyplot as plt
#
#from prophet import Prophet
#from datetime import datetime
#
pinkwink_web = pd.read_csv('https://raw.githubusercontent.com/PinkWink/DataScience/master/data/08.%20PinkWink%20Web%20Traffic.csv', encoding='utf-8', thousands=',', names = ['date','hit'], index_col=0)
pinkwink_web = pinkwink_web[pinkwink_web['hit'].notnull()]
#print(pinkwink_web.head())

#pinkwink_web['hit'].plot(figsize=(12,4), grid=True);
#
#구간 설정
time = np.arange(0,len(pinkwink_web))
traffic = pinkwink_web['hit'].values

fx = np.linspace(0, time[-1], 1000)

# 1,2,3,15차 함수로 회귀
fp1 = np.polyfit(time, traffic, 1)
f1 = np.poly1d(fp1)

f2p = np.polyfit(time, traffic, 2)
f2 = np.poly1d(f2p)

f3p = np.polyfit(time, traffic, 3)
f3 = np.poly1d(f3p)

f15p = np.polyfit(time, traffic, 15)
f15 = np.poly1d(f15p)

plt.figure(figsize=(12,4))
plt.scatter(time, traffic, s=10)

plt.plot(fx, f1(fx), lw=4, label='f1')
plt.plot(fx, f2(fx), lw=4, label='f2')
plt.plot(fx, f3(fx), lw=4, label='f3')
plt.plot(fx, f15(fx), lw=4, label='f15')

plt.grid(True, linestyle='-', color='0.75')

plt.legend(loc=2)
plt.show()
#