# ex01.py
from math import exp,log, sqrt
import re #regular expression  정규 표현식
from datetime import date, time, datetime, timedelta
from operator import itemgetter
import sys

input_file=sys.argv[1] # 시스템 도스창에 입력한 내용의 인덱스[1]출력 py ex01.txt 출력
print("Output")
with open(input_file,'r', newline='') as filereader : #new line='' - 줄바꿈 기호
    for row in filereader :
        print("{}".format(row.strip()))
#with : 자원을 얻은 다음에 클로즈해야하는 경우에 자동클로즈를 해주는 문법 규칙