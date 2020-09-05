
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 12:46:03 2017
 
@author: kkim
 
http://bit.ly/2019pcamp
"""
# 코딩 4원칙
# 1. 생각후코딩
# 2. 조건과반복
# 3. 읽기와쓰기
# 4. 주기와받기
#from math import exp, log, sqrt
#import re
#from datetime import date, time, datetime, timedelta
#from operator import itemgetter
#import glob
#
# #1: Print a simple string
#print("Why not change the world?")
#a = 10
#print(a)
#
## #2: Add two numbers together
#x = 4
#y = 5
#z = x + y
#print("z={0:d}.".format(z))
# "z={0:d}.".format(z) 를 분해하면
# "z={0:d}."문자열에 . format(z) 함수가 붙어있음
# 어떤문자열객체에 format함수를 호출함
# printf("%d %d",a,b);
#객체에 뭔가를 요청하는 것.
#어떤객체.어떤메소드(함수)
#
## #3: Add two lists together
#a = [1, 2, 3, 4]
#b = ["first", "second", "third", "fourth"]
#c = a + b
#print("a={0}, b={1}, c={2}".format(a, b, c))
#
## #4: INTEGERS
#x = 9
#print(x)
#print(3**4)
#print(int(8.3)/int(2.7))
# 엄밀하게 따지면 int()함수가 아니라 int객체의 생성자호출임 
# in C, (int)8.3
#
## #5: FLOATING-POINT NUMBERS
#print("{0:.3f}".format(8.3/2.7))
#y = 2.5*4.8
#print("{0:.1f}".format(y))
#r = 8/float(3)
#print("{0:.2f}".format(r))
#print("{0:.4f}".format(8.0/3))
#
## #6: Some mathematical functions available in the math module
#from math import exp, log, sqrt
#print("{0:.4f}".format(exp(3)))
#print("{0:.2f}".format(log(4)))
#print("{0:.1f}".format(sqrt(81)))
#
## #7: STRINGS
## A string with single quotes
#print("I'm enjoying learning \"Python\"")
#
## A long string
#print("first line second line")
#
## Use triple single or double quotes
#print('''You can use triple single quotes
#for multi-line comment strings''')
#
#print("""You can also use triple double quotations
#for multi-line comment strings""")
#
## Add two strings together
#string1 = "Hello "
#string2 = "World"
#sentence = string1 + string2
#print(sentence)
#
## Repeat a string four times
#print("She is", "very "*4, "beautiful.")
#
## number of characters in a string
#m = len(sentence)
#print("length : {0:d}".format(m))
#
## split()
#string1 = "Why not change the world?"
#string1_list1 = string1.split()
#print("string1_list1")
#print("FIRST PIECE:{0} SECOND PIECE:{1} THIRD PIECE:{2}"\
#.format(string1_list1[0], string1_list1[1], string1_list1[2]))
#string1_list2 = string1.split(" ", 2)
#print("string1_list2")
#print("FIRST PIECE:{0} SECOND PIECE:{1} THIRD PIECE:{2}"\
#.format(string1_list2[0], string1_list2[1], string1_list2[2]))
## delimeter
#string2 = "one,two,three,four,five,six"
#string2_list = string2.split(',')
#print(string2_list)
#print("{0} {1} {2}".format(string2_list[1], string2_list[5], string2_list[-1]))
#
## join()
#print("Output #25: {0}".format(','.join(string2_list)))
#
## strip()
#string3 = " Why not change the world?\t\t \n"
#print("<-{0:s}->".format(string3))
#string3_lstrip = string3.lstrip()
#print("<-{0:s}->".format(string3_lstrip))
#string3_rstrip = string3.rstrip()
#print("<-{0:s}->".format(string3_rstrip))
#string3_strip = string3.strip()
#print("<-{0:s}->".format(string3_strip))
#
#string4 = "$$Why not change the world?__---++"
#print("<-{0:s}->".format(string4))
#string4_strip = string4.strip('$_-+')
#print("<-{0:s}->".format(string4_strip))
#
## replace()
#string5 = "Why not change the world?"
#string5_replace = string5.replace(" ", "_")
#print("<-{0:s}->".format(string5_replace))
#string5_replace = string5.replace(" ", ",")
#print("<-{0:s}->".format(string5_replace))
#
## lower(), upper(), capitalize()
#string6 = "Why not CHANGE the world?"
#print("<-{0:s}->".format(string6.lower()))
#print("<-{0:s}->".format(string6.upper()))
#print("<-{0:s}->".format(string6.capitalize()))
#string8_list = string6.split()
#
#print("each words:")
#for word in string8_list:
#    print("{0:s}".format(word.capitalize()))
#
## #8: REGULAR EXPRESSIONS / PATTERN MATCHING
## Count the number of times a pattern appears in a string
#import re
#string = "Why not change the world?"
#string_list = string.split()
#pattern = re.compile(r"The", re.I)
#count = 0
#for word in string_list:
#   if pattern.search(word):
#       count += 1
#print("count : {0:d}".format(count))
 
## Substitute the letter "a" for the word "the" in the string
#string = "Why not change the world?"
#string_to_find = r"The"
#pattern = re.compile(string_to_find, re.I)
#print(pattern.sub("a", string))
#
## #9: DATES
#from datetime import date, time, datetime, timedelta
#today = date.today()
#print(today)
#print(today.year)
#print(today.month)
#print(today.day)
#current_datetime = datetime.today()
#print(current_datetime)
#
## Calculate a new date using a timedelta
#one_day = timedelta(days=-1)
#yesterday = today + one_day
#print(yesterday)
#eight_hours = timedelta(hours=-8)
#print(eight_hours.days, eight_hours.seconds)
#
## Calculate the amount of time between two dates and grab the first element, the number of days
#date_diff = today - yesterday
#print(date_diff)
#print(str(date_diff).split()[0])
#
## Create a string with a specific format from a date object
#print(today.strftime('%m/%d/%Y'))
#print(today.strftime('%b %d, %Y'))
#print(today.strftime('%Y-%m-%d'))
#print(today.strftime('%B %d, %Y'))
#
## Create a datetime object with a specific format from a string representing a date
#date1 = today.strftime('%m/%d/%Y')
#date2 = today.strftime('%b %d, %Y')
#date3 = today.strftime('%Y-%m-%d')
#date4 = today.strftime('%B %d, %Y')
#
## Two datetime objects and two date objects
## based on the four strings that have different date formats
#print(datetime.strptime(date1, '%m/%d/%Y'))
#print(datetime.strptime(date2, '%b %d, %Y'))
#
## Show the date portion only
#print(datetime.date(datetime.strptime(date3, '%Y-%m-%d')))
#print(datetime.date(datetime.strptime(date4, '%B %d, %Y')))
#
## #10: LISTS
## len() counts the number of elements in a list
## max() and min() find the maximum and minimum numbers in numeric lists
## count() counts the number of times a value appears in a list
#a_list = [1, 2, 3]
#print(a_list)
#print(len(a_list))
#print(max(a_list))
#print(min(a_list))
#another_list = ['printer', 5, ['star', 'circle', 9]]
#print(another_list)
#print(len(another_list))
#print(another_list.count(5))
#
## [0] is the first value; [-1] is the last value
#print(a_list[0])
#print(a_list[1])
#print(a_list[2])
#print(a_list[-1])
#print(a_list[-2])
#print(a_list[-3])
#print(another_list[2])
#print(another_list[-1])
#
## Use list slices to access a subset of list values
#print(a_list[0:2])
#print(another_list[:2])
#print(a_list[1:3])
#print(another_list[1:])
#
## Use [:] to make a copy of a list
#a_new_list = a_list[:]
#print(a_new_list)
#
## Use + to add two or more lists together
#a_longer_list = a_list + another_list
#print(a_longer_list)
#
## Use 'in' and 'not in' to check whether specific values are or are not in a list
#a = 2 in a_list
#print(a)
#if 2 in a_list:
#   print("2 is in {}.".format(a_list))
#b = 6 not in a_list
#print(b)
#if 6 not in a_list:
#   print("6 is not in {}.".format(a_list))
#
## Use append() to add additional values to the end of the list
## Use remove() to remove specific values from the list
## Use pop() to remove values from the end of the list
#a_list.append(4)
#a_list.append(5)
#a_list.append(6)
#print("a_list))
#a_list.remove(5)
#print("a_list)
#a_list.pop()
#a_list.pop()
#print(a_list)
#
## Use reverse() to reverse a list, in-place, meaning it changes the list
## To reverse a list without changing the original list, make a copy first
#a_list.reverse()
#print("a_list)
#a_list_copy = a_list[:]
#a_list_copy.reverse()
#print(a_list_copy)
#
## Use sort() to sort a list, in-place, meaning it changes the list
## To sort a list without changing the original list, make a copy first
#unordered_list = [3, 5, 1, 7, 2, 8, 4, 9, 0, 6]
#print(unordered_list)
#list_copy = unordered_list[:]
#list_copy.sort()
#print(list_copy)
#print(unordered_list)
#
## Use sorted() to sort a collection of lists by a position in the lists
#my_lists = [[1,2,3,4], [4,3,2,1], [2,4,1,3]]
#my_lists_sorted_by_index_3 = sorted(my_lists, key=lambda index_value: index_value[3])
#print(my_lists_sorted_by_index_3)
#
## Use itemgetter() to sort a collection of lists by two index positions
#my_lists = [[123,2,2,444], [22,6,6,444], [354,4,4,678], [236,5,5,678], [578,1,1,290], [461,1,1,290]]
#my_lists_sorted_by_index_3_and_0 = sorted(my_lists, key=itemgetter(3,0))
#print(my_lists_sorted_by_index_3_and_0)
#
## #11: TUPLES
## Use parentheses to create a tuple
#my_tuple = ('x', 'y', 'z')
#print(my_tuple)
#print(len(my_tuple))
#print(my_tuple[1])
#longer_tuple = my_tuple + my_tuple
#print(longer_tuple)
#
## Unpack tuples with the left-hand side of an assignment operator
#one, two, three = my_tuple
#print(one, two, three)
#var1 = 'handong'
#var2 = 'university'
#print(var1, var2)
## Swap values between variables
#var1, var2 = var2, var1
#print(var1, var2)
#
## Convert tuples to lists and lists to tuples
#my_list = [1, 2, 3]
#my_tuple = ('x', 'y', 'z')
#print(tuple(my_list))
#print(list(my_tuple))
#
## #12: DICTIONARIES
## Use curly braces to create a dictionary
## Use a colon between keys and values in each pair
## len() counts the number of key-value pairs in a dictionary
#empty_dict = { }
#a_dict = {'one':1, 'two':2, 'three':3}
#print(a_dict)
#print(len(a_dict))
#another_dict = {'x':'printer', 'y':5, 'z':['star', 'circle', 9]}
#print(another_dict)
#print(len(another_dict))
#
## Use keys to access specific values in a dictionary
#print(a_dict['two'])
#print(another_dict['z'])
#
## Use copy() to make a copy of a dictionary
#a_new_dict = a_dict.copy()
#print(a_new_dict)
#
## Use keys(), values(), and items() to access
## a dictionary's keys, values, and key-value pairs, respectively
#print(a_dict.keys())
#print(a_dict.values())
#print(a_dict.items())
#
## Use in, not in, and get to test
## whether a key is in a dictionary
#if 'y' in another_dict:
#   print("y is a key in another_dict: {}.".format(another_dict.keys()))
#
#if 'c' not in another_dict:
#   print("c is not a key in another_dict: {}.".format(another_dict.keys()))
#
#print("three: {!s}".format(a_dict.get('three')))
#print("four: {!s}".format(a_dict.get('four')))
#print("four: {!s}".format(a_dict.get('four', 'Not in dict')))
#
## Use sorted() to sort a dictionary
## To sort a dictionary without changing the original dictionary,
## make a copy first
#print(str(a_dict))
#dict_copy = a_dict.copy()
#ordered_dict1 = sorted(dict_copy.items(), key=lambda item: item[0])
#print("order by keys: {}".format(ordered_dict1))
#ordered_dict2 = sorted(dict_copy.items(), key=lambda item: item[1])
#print("order by values: {}".format(ordered_dict2))
#ordered_dict3 = sorted(dict_copy.items(), key=lambda x: x[1], reverse=True)
#print("order by values, descending)=: {}".format(ordered_dict3))
#ordered_dict4 = sorted(dict_copy.items(), key=lambda x: x[1], reverse=False)
#print("order by values, ascending: {}".format(ordered_dict4))
#
## #13 CONTROL FLOW
## if-else statement
#x = 5
#if x > 4 or x != 9:
#    print("x: {}".format(x))
#else:
#    print("x is not greater than 4")
#
## if-elif-else statement
#if x > 6:
#    print("x is greater than six")
#elif x > 4 and x == 5:
#    print(x*x)
#else:
#    print("x is not greater than 4")
#
## for loop
#y = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', \
#'Nov', 'Dec']
#z = ['Annie', 'Betty', 'Claire', 'Daphne', 'Ellie', 'Franchesca', 'Greta', \
#'Holly', 'Isabel', 'Jenny']
#
#for month in y:
#    print(month)
#
#print("index value: name in list")
#for i in range(len(z)):
#    print(i, z[i])
#
#print("access elements in y with z's index values")
#for j in range(len(z)):
#    if y[j].startswith('J'):
#        print(y[j])
#
#for key, value in another_dict.items():
#    print(key, value)
#
## compact for loops
## list, set, and dictionary comprehensions
## Select specific rows using a list comprehension
#my_data = [[1,2,3], [4,5,6], [7,8,9]]
#rows_to_keep = [row for row in my_data if row[2] > 5]
#print(rows_to_keep)
#
## Select a set of unique tuples in a list using a set comprehension
#my_data = [(1,2,3), (4,5,6), (7,8,9), (7,8,9)]
#set_of_tuples1 = {x for x in my_data}
#print(set_of_tuples1)
#set_of_tuples2 = set(my_data)
#print(set_of_tuples2)
#
## Select specific key-value pairs using a dictionary comprehension
#my_dictionary = {'customer1': 7, 'customer2': 9, 'customer3': 11}
#my_results = {key : value for key, value in my_dictionary.items() if \
#value > 10}
#print(my_results)
#
## while loop
#x = 0
#while x < 11:
#    print(x)
#    x += 1
#
## #14: FUNCTIONS
## Calculate the mean of a sequence of numeric values
#def getMean(numericValues):
#    return sum(numericValues)/len(numericValues) if len(numericValues) > 0 \
#    else float('nan')
#
#my_list = [2, 2, 4, 4, 6, 6, 8, 8]
#print("getMean(my_list))
#
## #15: FILE
# READ A FILE
# Read a single text file
#input_file = "test.txt"
# 
## Read a text file (older method) ##
#filereader = open(input_file, 'r', newline='')
#for row in filereader:
#    print(row.strip())
#filereader.close()
 
## Read a text file (newer method) ##
#with open(input_file, 'r', newline='') as filereader:
#    for row in filereader:
#        print(row.strip())
 
# READ MULTIPLE FILES
# Read multiple text files
#import glob, os
#inputPath = './'
#for input_file in glob.glob(os.path.join(inputPath,'*.txt')):
#    with open(input_file, 'r', newline='') as filereader:
#       for row in filereader:
#           print(row.strip())
 
# WRITE TO A FILE
# Write to a text file
#my_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
#max_index = len(my_letters)
#output_file = "outputtest.txt"
#filewriter = open(output_file, 'w')
#for index_value in range(len(my_letters)):
#    if index_value < (max_index-1):
#        filewriter.write(my_letters[index_value]+'---')
#    else:
#        filewriter.write(my_letters[index_value]+'\n')
#filewriter.close()
#print("Output written to file")
 
## Write to a CSV file
#my_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#max_index = len(my_numbers)
#output_file = "output.csv"
#filewriter = open(output_file, 'a')
#for index_value in range(len(my_numbers)):
#    if index_value < (max_index-1):
#        filewriter.write(str(my_numbers[index_value])+'')
#    else:
#        filewriter.write(str(my_numbers[index_value])+'\n')
#filewriter.close()
#print("Output appended to file")
#
#import pandas as pd
#scores = pd.read_csv()
