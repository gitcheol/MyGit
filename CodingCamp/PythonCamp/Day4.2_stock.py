#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 주식 데이터 가져오기 
from pandas_datareader import data
import matplotlib.pyplot as plt
import fix_yahoo_finance as yf


yf.pdr_override()

start_date = '2000-1-1' 
end_date = '2019-1-31' 
KIA = data.get_data_yahoo('000270.KS', start_date, end_date)
NAVER = data.get_data_yahoo('035420.KS', start_date, end_date)
   
print(KIA.columns)

plt.figure(figsize=(12,6))
plt.plot(KIA['Close'], label='KIA')
plt.plot(NAVER['Close'], label='Naver')
plt.legend(loc=2)

plt.grid()
plt.show()