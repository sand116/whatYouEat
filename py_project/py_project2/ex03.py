# ex01.py
from math import exp,log, sqrt
import re #regular expression  정규 표현식
from datetime import date, time, datetime, timedelta
from operator import itemgetter
import sys
import os
import glob

 #현재 폴더에 있는것 다 찾아줌 : python ex03.py #C:\Users\박진경\Desktop\py_project\py_project2
 
print("output")

input_path= sys.argv[1] #C:\Users\박진경\Desktop\py_project\py_project2
print(os.path.join(input_path,"*.txt"))
#C:\Users\박진경\Desktop\py_project\py_project2\*.txt
for input_file in glob.glob(os.path.join(input_path,"*.txt")) :
    with open(input_file,'r',newline='') as filereader:
        for row in filereader:
            print("{}".format(row.strip()))
#첫글자가 대문자면 클래스/ 소문자면 변수 or 함수 해당 변수는 inputPass
#상수형 변수이면 모든 것을 대문자로 표현