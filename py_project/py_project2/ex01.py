# ex01.py
from math import exp,log, sqrt
import re #regular expression  정규 표현식
from datetime import date, time, datetime, timedelta
from operator import itemgetter
import sys

print("Output")
input_file=sys.argv[1] # 시스템 도스창에 입력한 내용의 인덱스[1]출력 py ex01.txt 출력
#python ex01.py ex01.txt
#   0   1
filereader=open(input_file,'r') #r=read 일기전용으로 열겠다
for row in filereader :
    print(row.strip())
filereader.close()
print(sys.argv[0])
#close  꼭 해줘야하는 경우 1. 파일 작업 2. db 항상 클로즈