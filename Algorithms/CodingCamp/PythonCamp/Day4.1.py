#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 11:07:27 2019

##source from 
https://github.com/PinkWink/DataScience/blob/master/source_code/01.%20Basic%20of%20Python%2C%20Pandas%20and%20Matplotlib%20%20via%20analysis%20of%20CCTV%20in%20Seoul.ipynb
"""
import pandas as pd


#행병합
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'], 
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                   index=[0, 1, 2, 3])

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']},
                   index=[4, 5, 6, 7])

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                    'B': ['B8', 'B9', 'B10', 'B11'],
                    'C': ['C8', 'C9', 'C10', 'C11'],
                    'D': ['D8', 'D9', 'D10', 'D11']},
                   index=[8, 9, 10, 11])

#print(df1)
#print(df2)
#print(df3)

#M1 = pd.concat([df1, df2, df3])
#print(M1)
##
#M1 = pd.concat([df1, df2, df3], keys=['x', 'y', 'z']) #어디서 온 data인지 Key값을 줌
#print(M1)#2-D Array처럼 in row there are level.
#
#print(M1.index) # level and index
#print(M1.index.get_level_values(0)) #
#
### 열병합
#
#df4 = pd.DataFrame({'B': ['B2', 'B3', 'B6', 'B7'], 
#                    'D': ['D2', 'D3', 'D6', 'D7'],
#                    'F': ['F2', 'F3', 'F6', 'F7']},
#                   index=[2, 3, 6, 7])
#print(df1)
#print(df4)
#M2 = pd.concat([df1, df4], axis=1)
#print(M2)
#index가 겹치는 애들만 합치겠다.
#M2 = pd.concat([df1, df4], axis=1, join='inner')
#print(M2)
#index가 기준 df1애 있는 애들만 합치겠다.
#M2 = pd.concat([df1, df4], axis=1, join_axes=[df1.index])
#print(M2)
#sort=False 써줘야 된다네 ; index가 같으면 merge 이런식.
#M2 = pd.concat([df1, df4], ignore_index=True)
#print(M2)
#
##Merge

left = pd.DataFrame({'key': ['K0', 'K4', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})

right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})

print(left)
print(right)

##common key values merged.
#M3 = pd.merge(left, right, on='key')
#print(M3)
#
##standart is left, olny in left keys will be merged
#M3 = pd.merge(left, right, how='left', on='key')
#print(M3)
#
##standart is left, olny in right keys will be merged
#M3 = pd.merge(left, right, how='right', on='key')
#print(M3)
#
#M3 = pd.merge(left, right, how='inner', on='key')
#print(M3)
#
#M3 = pd.merge(left, right, how='outer', on='key')
#print(M3)