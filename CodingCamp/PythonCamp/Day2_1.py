#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 14:01:53 2019

@author: gichulkim
"""
from random import *

import numpy as np

list1=[1,2,3,4,5,6,7,8,9,0]
data=np.array(list1)
print(type(data))
#data=np.arange(0,10,1)
#
#print(data)
#print(data.shape)
#print(data.dtype)
#print(data.size)

#datalist=[[1,2,3],[10,20,30],[100,200,300],[1000,2000,3000]]
#data=np.array(datalist)
#print(data.shape)
#print(data.dtype)
#print(data.size)
#print(data)

##1차원 배열의 일부 원소들만 선택하기
#datalist=[0,1,2,3,4,5,6,7,8,9]
#data= np.array(datalist)
#print(data)
#print(data[5])
#print(data[5:8])
#data[3:6]=0
#print(data)
#   
#print(datalist)
##np.array일 때만 사용가능. 그냥 list에서 사용하면 오류
##datalist[3,5]=0
#print(datalist)

##2차원 배열의 일부 원소들만 선택하기
#datalist=[[1,2,3],[10,20,30],[100,200,300],[1000,2000,3000]]
#data=np.array(datalist)
#print(data)
#print(data[2])
#print(data[2][1])
#print(data[2,1])
#print(data[:2,1:])
#data[3]=0
#print(data)

##조건에 부합하는지 판단하는 불리언 배열 만들기
#datalist=[55,78,96,75,64,85,49,80,77,89]
#data=np.array(datalist)
#print(data)
#print(data>=60)

##특정 조건에 부합하는 원소만 새로운 값으로 할당하기
#datalist=[55,78,96,75,64,85,49,80,77,89]
#data=np.array(datalist)
#print(data)
#print(data<60)
#data[data<60] = 60
#print(data)

##배열끼리 연산하기
#kor=np.random.randint(55,100,10)
#eng=np.random.randint(55,100,10)
#mat=np.random.randint(55,100,10)
#print(kor)
#print(eng)
#print(mat)
#avg=(kor+eng+mat)/3
#print(avg)

##배열의 원소 이름을 정해 부르기
#datalist=[(86,93,73),(67,90,85),(90,80,70)]
#score=np.array(datalist,dtype=[('kor','i4'),('eng','i4'),('mat','i4')])
#print(score)
#print(score['eng'])
#print(score[1]['kor'])

##배열을 사용한 데이터 고르기
#numbers1=np.random.randint(1,100,10)
#numbers2=np.random.randint(1,100,10)
#compare=np.array(numbers1>numbers2)

##조건 판달결과를 반영한 배열 만들기
#numbers=np.random.randint(50,100,10)
#score=np.where(numbers>=70,'Pass','Fail')
#print(numbers)
#print(score)

##np.array의 메소드 사용하기
#numbers=np.random.randint(1,100,10)
#print(numbers)
#print(numbers.max())
#print(numbers.min())
#print(numbers.sum())
#print(numbers.mean())
#print(numbers.std())
#print(numbers.cumsum())
#numbers.sort()
#print(numbers)

##벡터 연산
#d=np.array([5,0])
#e=np.array([3,6])
#f=d+e
#print(f)
#f=d-e
#print(f)

##linspace  -- np array를 만드는 방법 #3  (#2는 arange #1은 배열을 넣는것)
#points=np.linspace(-5,5,num=11)
#print(points)
#points=np.linspace(-5,5,num=10,endpoint=False)
#print(points)
#points=np.linspace(-5,5,3)
#print(points)

##Random3  numbers file write
#import string
#from random import randint, choice
#f=open("numdata3.txt","w")
#for i in range(100):
#    f.write("%d %d %d\n"%(randint(50,100),randint(50,100),randint(50,100)))
#
#randomstr=''.join(choice(string.ascii_uppercase))for _ in range(3):
#    f.write("%s %d %d %d\n"%(randomstr,randint(50,100),randint(50,100),randint(50,100)))
#
#f.close()

#1번 방법 : 숫자만 있는 경우
#scores=np.genfromtxt('numdata3.txt',names=('KOR','ENG','MAT'))
#print(scores)

#2번 방법 : 문자열과 숫자만 섞여 있는 경우
#scores=np.genfromtxt('numdata2.txt')


#3번 방법 : Header 있는 경우














