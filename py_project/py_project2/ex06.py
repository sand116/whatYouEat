# ex01.py
from math import exp,log, sqrt
import re #regular expression  정규 표현식
from datetime import date, time, datetime, timedelta
from operator import itemgetter
import sys
import os
import glob

my_numbers =[0,1,2,3,4,5,6,7,8,9]
max_index=len(my_numbers)
output_file=sys.argv[1]

#python ex06.py ex06.csv # comma seperate value

filewriter=open(output_file,'a') #append : 추가
for i in range(max_index) :
    if i < (max_index-1) :
        filewriter.write(str(my_numbers[i])+',')
    else :
        filewriter.write(str(my_numbers[i])+'\n')
filewriter.close()
print('output')
#W옵션은 덮어쓰기 해서 실행할때마다 덮어쓰는 반면, 'a'는 실행할때마다 추가하면서 들어간다