#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 10:17:11 2019

@author: gichulkim
"""
#csv version and pandas version




##조건을 줘서 해당되는 특정 row들을 출력 
#import csv 
#
#input_file = "p_20180930.csv"
#output_file = "p_20180930_4.txt"
#
#csv_in_file = open(input_file, 'r',newline='')
#csv_out_file = open(output_file, 'w',newline='')
#
#filereader=csv.reader(csv_in_file)
#filewriter=csv.writer(csv_out_file)
#
#header=next(filereader)
#filewriter.writerow(header)
#
#for row_list in filereader:
#    ptype=str(row_list[3]).strip()
#    psize=str(row_list[6]).replace(',','')
#    if ptype == '노상' and int(psize)>30:
#        filewriter.writerow(row_list)
#
#csv_in_file.close()
#csv_out_file.close()

##loc = 부분집합을 의미
#import pandas as pd
#
#input_file = "p_20180930.csv"
#output_file= "p_20180930_6.txt"
#
#data_frame=pd.read_csv(input_file)
#
#my_pattern=data_frame.loc[data_frame['소재지도로명주소'].str.startswith("경상북도 포항시 북구"),:]
##data_frame['주차구획수']=data_frame['주차구획수'].astype(float)
##my_condition=data_frame.loc[(data_frame['주차장유형'].str.contains('노상'))&(data_frame['주차구획수']>30), :]
#
#my_pattern.to_csv(output_file,index=False)






##특정 data의 row write

#import csv
#important_dates=['2010.01','2011.01']
#input_file = "p_20180630.csv"
#output_file="p_20180630_7.txt"
#
#csv_in_file=open(input_file,'r', newline='')
#csv_out_file=open(output_file,'w', newline='')
#
#filereader=csv.reader(csv_in_file)
#filewriter=csv.writer(csv_out_file)
#
#header=next(filereader)
#filewriter.writerow(header)
#
#for row_list in filereader:
#    a_date=row_list[0]
#    if a_date in important_dates:
#        filewriter.writerow(row_list)
#        
#csv_in_file.close()
#csv_out_file.close()

#import pandas as pd
#
#important_dates=['2010.01', '2011.01']
#input_file = "p_20180630.csv"
#output_file= "p_20180630_8.txt"
#
#data_frame=pd.read_csv(input_file)
#
#my_set=data_frame.loc[data_frame['년월'].isin(important_dates),:]
#
#
#my_set.to_csv(output_file,index=False)

##column만 뽑아내기
#import csv
#my_columns=[0,1,2]
#input_file = "p_20180630.csv"
#output_file="p_20180630_9.txt"
#
#csv_in_file=open(input_file,'r', newline='')
#csv_out_file=open(output_file,'w', newline='')
#
#filereader=csv.reader(csv_in_file)
#filewriter=csv.writer(csv_out_file)
#
#for row_list in filereader:
#    row_list_output=[]
#    for index_value in my_columns:
#        row_list_output.append(row_list[index_value])
#    filewriter.writerow(row_list_output)
#        
#csv_in_file.close()
#csv_out_file.close()

#import pandas as pd
#
#input_file = "p_20180630.csv"
#output_file= "p_20180630_10.txt"
#
#data_frame=pd.read_csv(input_file)
#
#my_index=data_frame.iloc[:,[0,1,2]]
#
#my_index.to_csv(output_file,index=False)




###indexing이 아니라 string로 추가.
#import csv
#my_columns=['년월', ' 한국인남 ', ' 한국인여 ']
#my_columns_index=[]
#
#input_file = "p_20180630.csv"
#output_file="p_20180630_11.txt"
#
#csv_in_file=open(input_file,'r', newline='')
#csv_out_file=open(output_file,'w', newline='')
#
#filereader=csv.reader(csv_in_file)
#filewriter=csv.writer(csv_out_file)
#header=next(filereader)
#
#for index_value in range(len(header)): #finding columnindex
#    if header[index_value] in my_columns:
#        my_columns_index.append(index_value)
#filewriter.writerow(my_columns)
#
#for row_list in filereader:
#    row_list_output=[]
#    for index_value in my_columns_index:
#        row_list_output.append(row_list[index_value])
#    filewriter.writerow(row_list_output)
#        
#csv_in_file.close()
#csv_out_file.close()

#import pandas as pd
#
#input_file = "p_20180630.csv"
#output_file= "p_20180630_12.txt"
#my_columns=['년월',' 한국인남 ', ' 한국인여 ']
#
#data_frame=pd.read_csv(input_file)
#
#my_data=data_frame.loc[:,my_columns]
#
#my_data.to_csv(output_file,index=False)












