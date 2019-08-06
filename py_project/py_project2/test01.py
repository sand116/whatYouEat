#join - ','.join 리스트 문자열로 바꿀 때! -데이터를 하나씩 꺼내어서 ,으로 연결하고 싶다
#map    : 하나씩 처리
#reduce : 줄인다(합친다 등)

c=[1,2,3,4,5]

d=[]
for i in c:
    x=i**2
    d.append(x)
print(d)


#위의 반복문을 MAP을 이용하여 처리하겠다
def square(x):
    return x**2
e=map(square,c) #map도 lazy loading 이라 list함수처리해줘야함.
print(list(e))

#하둡 = HDFS(데이터 저장 하둡 분산 저장 시스템) + map,reduce (데이터 처리)
# 하둡의 MAP, REDUCE가 자바형(OP언어)이라 무거워서 SPARK로 변환 (함수형 언어)

# lambda 표헌식 - 익명함수 규칙 (이름이 없다)
# lambda x: x**2

f=map(lambda x: x**2,c)
print(list(f))

g=['Supplier Name',100,'Part Number','Cost','Purchase Date']
h=map(str,g) #숫자 100에 str 함수 적용
print(list(h))

from functools import reduce
i=range(1,11) #1부터 10까지

def add(x,y) :
    return x+y

j=reduce(add,i) #덧셈해라 i에있는 연속된 값을 가지고
print(j)
######################### 고차함수 - 함수를 호출할수 있는 함수
j=reduce(lambda x,y : x+y, i) #선언적 코딩 ->내부 반복문
