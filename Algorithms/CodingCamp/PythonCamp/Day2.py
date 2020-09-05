#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 16:12:32 2019

@author: gichulkim
"""

#input_file = "p_20180930.csv" #포항시 주차장 정보 파일
#output_file = "p_20180930.txt" #출력 파일#1
#
#filereader = open(input_file, 'r', newline='')
#filewriter = open(output_file,'w',newline='')
#header = filereader.readline()
#header = header.strip()
#header_list=header.split(',')
#print(header_list)
#filewriter.write('/'.join(header_list)+'\n')
#for row in filereader :
#    row = row.strip()
#    row_list=row.split(',')
#    print(row_list)
#    filewriter.write('/'.join(row_list)+'\n')
#    
#filereader.close()
#filewriter.close()

#import csv
#
#input_file = "p_20180930.csv"
#output_file= "p_20180930_2.txt"
#
#csv_in_file=open(input_file,'r',newline='')
#csv_out_file=open(output_file,'w',newline='')
#filereader= csv.reader(csv_in_file,delimiter=',')
#filewriter= csv.writer(csv_out_file,delimiter='/')
#for row_list in filereader : 
#    filewriter.writerow(row_list)
#csv_in_file.close()
#csv_out_file.close()

#import pandas as pd
#
#input_file = "p_20180930.csv"
#output_file= "p_20180930_3.txt"
#
#data_frame=pd.read_csv(input_file)
#print(data_frame)
#data_frame.to_csv(output_file,index=False)