# 파일 처리 --> 내장함수

'''
파일 오픈 : open(파일명,엑세스모드,버퍼링)
엑세스 모드 :
r ->읽기 모드
b ->바이너리 이진형식으로 ~
w ->쓰기모드
+ ->반대 속성이 추가된
r+ -> 읽고 쓰기 모드
a -> 추가,덧붙이기
a+ -> 덧붙이고 읽기
ab ->이진형식으로 덧붙이기
버퍼링 :
0 : 안함
1: 라인별 버퍼링
-1(음수) : 버퍼링하는 크기를 시스템 크기에 맞춤
1이상 : 버퍼링크기 부여함
'''
# 파일 I/O ->입/출력 -> 반드시 사용이 끝나면 닫아야 한다. 
# 파일이 없으면 만들어서 오픈
# f = open('test.txt','w',)

# # f.close()

# f=open("test.txt","r+")
# s=f.read(2) #2byte읽겠다
# print(s,f.tell()) #현재 파일 포인터 위치
# f.seek(4) #파일 포인터를 처음 위치 기준에서 이동
# s=f.read(2)
# print(s,f.tell())
# f.close()

f=open('t1.txt','w')
for n in range(10):
    str="%d line(라인)\n"%n
    f.write(str)
f.close()

f=open("t1.txt",'r')
while True :
    #한줄씩 읽는다
    data=f.readline()
    if not data:
        break
    print(data)
f.close()

#파이썬은 i/o에서 닫는 부분을 자동으로 처리해주는 기능을 가지고 있음
with open("t1.txt",'r') as f :
    while True :
        #한줄씩 읽는다
        data=f.readline()
        if not data:
            break
        print(data)

#외장 함수 : 구조화된 모듈 저장 획로드
#피클
import pickle as p
data={
    1:[1,2,3,4],
    2:{'name':'multi'},
    3:(5,6,7,8)
}
#기록
with open("data.p","wb") as f1:
    p.dump(data, f1,p.HIGHEST_PROTOCOL)
#로드 -> 데이터를 원래대로 복구
with open("data.p","rb") as f1:
    tmp=(p.load(f1))
    print(tmp,type(tmp))

#################################################################
#os 모듈
import os
print("현재 프로젝트 디렉토리(운영체제 관계없이)",os.getcwd())
os.mkdir("tmp")
os.chdir("tmp")
print(os.getcwd())
os.chdir("..")
print(os.getcwd())