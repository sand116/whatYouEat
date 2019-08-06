# ex01.py
from math import exp,log, sqrt
import re #regular expression  정규 표현식
from datetime import date, time, datetime, timedelta
from operator import itemgetter
import sys
import os
import glob
#python ex04.py ex04.tsv
my_letters = [ 'a','b','c','d','e','f','g','h','i','j']
max_index=len(my_letters)
output_file=sys.argv[1] #결과 값을 ex04.csv로 저장한다.
filewriter=open(output_file,'w') #파일 작성한다.
for index_value in range(max_index) :
    if index_value<(max_index-1) :
        filewriter.write(my_letters[index_value]+'\t')
    else :
        filewriter.write(my_letters[index_value]+'\n')
filewriter.close()
print('output')