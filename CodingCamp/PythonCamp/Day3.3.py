
#pandas
#cPython을 위한 데이터 분석 도구 http://pandas.pydata.org/
#Excel 데이터 읽고, 피벗 분석
#http://pinkwink.kr/977?category=522424
#Data Structure
#pandas exercises
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 00:35:34 2019

@author: kkim
"""

#◉ Series
# 
#import pandas as pd 
#data = [77,66,88,99,55] 
#obj = pd.Series(data) 
#print(obj) 
#print(obj.values) 
#print(obj.index)  #range(0,5,1)와 비슷
#print(obj[2])
#
#• 사용자 정의 index를 사용할 수 있음
#import pandas as pd
#data = [77,66,88,99,55]
#keys = ['Kim','Lee','Park','Jang','Hwang'] 
#obj = pd.Series(data, index=keys) 
#print(obj)
#print(obj.values)
#print(obj.index)
#print(obj['Kim'])
#obj['Kim'] = 95
#print(obj['Kim']) 
#print(obj[['Kim','Lee','Hwang']]) 
#print(obj[obj > 80])
#print('Oh' in obj)
#
#• 딕셔너리를 통해 Series 만들기
#import pandas as pd
#data = {'Kim':77,'Lee':66,'Park':88,'Jang':99,'Hwang':55} 
#obj = pd.Series(data)
#print(obj)
#
#• Series 간 연산
#import pandas as pd
#data1 = {'Kim':77,'Lee':66,'Park':88,'Jang':99,'Hwang':55} 
#obj1 = pd.Series(data1)
#data2 = {'Kim':87,'Lee':87,'Park':80,'Jang':69,'Hwang':85}
#obj2 = pd.Series(data2)
#print(obj1 + obj2)

#• reindex
#import pandas as pd
#data1 = {'Kim':77,'Lee':66,'Park':88,'Jang':99,'Hwang':55} 
#obj1 = pd.Series(data1)
#print(obj1)
#obj2 = obj1.reindex(['Kim','Park','Lee','Jang','Hwang']) #데이터말고 print되는 순서를 바꿔주는 것.
#print(obj2)
## 
#◉ DataFrame
#index를 공통으로 사용하고 있는 Series 객체들을 담고 있다고 생각하면 된다.
#
#• 딕셔너리로 Column 정보를 넣어서 생성
#import pandas as pd
#import matplotlib.pyplot as plt
#data = {'col1': [77,66,88,99,55],'col2': [45,56,67,78,89], 'col3': [97,86,75,64,53]}
#df = pd.DataFrame(data) 
#print(df)
#df.plot()
#
##• index 명 삽입
#import pandas as pd
##import matplotlib.pyplot as plt
#data = {'col1': [77,66,88,99,55],'col2': [45,56,67,78,89],'col3': [97,86,75,64,53]}
#keys = ['Kim','Lee','Park','Jang','Hwang']
#df = pd.DataFrame(data, index=keys) 
#print(df)
#df.plot()
#
#• Column 별로 만든 리스트를 묶어서 생성
#import pandas as pd
#import matplotlib.pyplot as plt
#kor = [77,66,88,99,55]
#eng = [45,56,67,78,89]
#mat = [97,86,75,64,53]
#data = list(zip(kor,eng,mat))
#keys = ['Kim','Lee','Park','Jang','Hwang']
#df = pd.DataFrame(data, index=keys, columns=['KOR','ENG','MAT']) 
##print(df)
#plt.plot(df)

#• 같은 키를 사용하는 여러 딕셔너리를 조합하여 생성
#import pandas as pd
#kor = {'Kim':77,'Lee':66,'Park':88,'Jang':99,'Hwang':55} 
#eng = {'Kim':45,'Lee':56,'Park':67,'Jang':78,'Hwang':89} 
#mat = {'Kim':97,'Lee':86,'Park':75,'Jang':64,'Hwang':53} 
#data = {'KOR':kor, 'ENG':eng, 'MAT':mat}
#df = pd.DataFrame(data)
#print(df)
#
#• 기존 Column을 이용하여 새로운 Column 추가
#import pandas as pd
#kor = {'Kim':77,'Lee':66,'Park':88,'Jang':99,'Hwang':55} 
#eng = {'Kim':45,'Lee':56,'Park':67,'Jang':78,'Hwang':89} 
#mat = {'Kim':97,'Lee':86,'Park':75,'Jang':64,'Hwang':53} 
#data = {'KOR':kor, 'ENG':eng, 'MAT':mat}
#df = pd.DataFrame(data)
#print(df)
#df['Sum']=df['KOR']+df['ENG']+df['MAT'] 
#df['Avg']=df['Sum']/3
#print(df)
#
#• reindex
#import pandas as pd
#kor = {'Kim':77,'Lee':66,'Park':88,'Jang':99,'Hwang':55}
#eng = {'Kim':45,'Lee':56,'Park':67,'Jang':78,'Hwang':89}
#mat = {'Kim':97,'Lee':86,'Park':75,'Jang':64,'Hwang':53}
#data = {'KOR':kor, 'ENG':eng, 'MAT':mat}
#df = pd.DataFrame(data)
#df['Sum']=df['KOR']+df['ENG']+df['MAT']
#df['Avg']=df['Sum']/3
#print(df)
#df2 = df.reindex(index=['Kim','Lee','Park','Jang','Hwang'],columns=['KOR','ENG','MAT','Su m','Avg'])
#print(df2)
#
#• 정렬
#import pandas as pd
#kor = [77,66,88,99,55]
#eng = [45,56,67,78,89]
#mat = [97,86,75,64,53]
#data = list(zip(kor,eng,mat))
#keys = ['Kim','Lee','Park','Jang','Hwang']
#df = pd.DataFrame(data, index=keys, columns=['KOR','ENG','MAT']) 
#df['Sum']=df['KOR']+df['ENG']+df['MAT']
#df['Avg']=df['Sum']/3
#print(df)
#df2 = df.sort_values('Sum', ascending=False) 
#print(df2)
#
#
# Reading from internet file
#import pandas as pd
#df = pd.read_csv('https://raw.githubusercontent.com/datascienceschool/docker_rpython/master/data/titanic.csv')
##print(df)
##df=data_frame.loc[data_frame['Survived'].isin('1'),:]
#df=df.sort_values('Pclass',ascending=False)
#
#print(df.head(3))
#print(df.tail(3))

###########################################
#Matplotlib
#
#◉ plot()
#import matplotlib.pyplot as plt 
#import numpy as np
##data=[1,2,3,4,5,6,7] 
##data=[4,5,6,1,2,3,7]   #y축 data가 됨 
##data = np.arange(1,20,0.1)
#plt.plot(data) 
#plt.ylabel('Values')
#plt.xlabel('sungmins')
#
#plt.show()

#import matplotlib.pyplot as plt 
#import numpy as np
#x = np.arange(0,10,0.1)
#y = np.sin(x)
#plt.figure(figsize=(10,4))
#plt.plot(x,y) 
#plt.grid()
#plt.xlabel('x')
#plt.ylabel('sin')
#plt.show()

 
#import numpy as np
#import matplotlib.pyplot as plt 
#import seaborn as sns 
#sns.set()
#x_data = np.linspace(0,10,500) 
#y_data = np.power(x_data,2) 
#plt.plot(x_data, y_data) 
#plt.ylabel('Values')
#plt.show()

#• 특정 좌표를 이어주는 그래프 그리기
#import matplotlib.pyplot as plt 
#import seaborn as sns 
#sns.set()
##x_data = [0,1,2,3,4,5,6] 
#y_data = [1,3,4,7,10,15,16] 
#colormap = x_data
#plt.plot(x_data, y_data) 
#plt.scatter(x_data, y_data, s=7, marker='>')
##plt.bar(x_data, y_data, width=0.5, color='c')
#plt.ylabel('Values')
#plt.show()

#• 그래프 2개 그리기
#import numpy as np
#import matplotlib.pyplot as plt 
#import seaborn as sns 
#sns.set()
#x_data = np.array([0,1,2,3,4,5,6]) 
#y_data1 = np.array([1,3,4,7,10,15,16]) 
#y_data2 = np.array([5,4,2,9,15,25,36])
#plt.plot(x_data, y_data1) 
#plt.plot(x_data, y_data2) 
#plt.bar(x_data, y_data1, width=0.3, color='r', label="Graph #1") 
#plt.bar(x_data+0.5, y_data2, width=0.3, color='g', label="Graph #2") 
#plt.barh(x_data, y_data1, color='r', label="Graph #1") 
#plt.barh(x_data, -y_data2, color='g', label="Graph #2") 
#plt.ylabel('Values')
#plt.pie(y_data1)
#plt.legend()
#plt.show()

#• 좌표 찍기
#import numpy as np
#import matplotlib.pyplot as plt 
#import seaborn as sns
#sns.set()
#x_values = np.linspace(0, 10, 20) 
#y_values = np.zeros(20) 
#print(x_values)
#print(y_values)
#plt.plot(x_values, y_values, 'o') 
#plt.plot(x_values, y_values+0.5, 'b^') 
#plt.ylim([-1,1])
#plt.show()

#legend()
#import numpy as np
#import matplotlib.pyplot as plt 
#import seaborn as sns
#sns.set()
#x_values = np.linspace(0, 10, 50) 
#y_values1 = np.sin(x_values) 
#y_values2 = np.cos(x_values) 
#plt.plot(x_values, y_values1, label='sin') 
#plt.plot(x_values, y_values2, 'r^', label='cos')  #plt에서 점 찍을 때 'r^'사용
#plt.xlim([0,2*np.pi])
#plt.legend()
#plt.show()
#
#• plot() 한번으로 여러 개의 좌표 찍기
#import numpy as np
#import matplotlib.pyplot as plt
#import seaborn as sns
#sns.set()
#x = np.linspace(0, 10, 10) 
##plt.plot(x,x,'o',x,x**2,'^',x,x**3,'s') #그래프 한번에 3개를 그린거
#plt.plot(x,x,'rs', x,x**2,'g^', x,x**3,'--') #그래프 모양까지
##red squares, green triangles, blue dashes 
##plt.xlim([0,2*np.pi])
#plt.show()

#• 2개의 리스트로 그래프 그리기
#import numpy as np
#import matplotlib.pyplot as plt
#import seaborn as sns
#sns.set()
#years = np.arange(2010, 2020)
#values = np.random.randint(500,2000,10) 
#plt.plot(years,values,'r^-') #red triangles solid line 
#plt.show()
#