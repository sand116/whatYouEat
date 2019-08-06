#참조 카운트 :객체 속성
import sys
#내장된 라이브러리
a = 1
print(a,type(a),sys.getrefcount(1)) #1을 참조하는 것이 몇개냐 
b=1
print(b,type(b),sys.getrefcount(b)) #1을 참조하는 것이 몇개냐 
print(a is b) #a와 b는 똑같은 것을 가르킨다.

del (a) #참조 끊기
print(sys.getrefcount(1))
# print (a is b)

#***파이썬에 존재하는 모든 요소는 객체다 (객체는 메모리에 상주)**
#파이썬에서 사용하는 것들 중에 예를 들어 1,2,3 이런것들도 객체고
#단지 참조를 통해서 해당 객체를 사용할 뿐이다

from a.b.mod import A
obj=A() 
print("객체 A : ", sys.getrefcount(A))
del(obj)
print("객체 A : ", sys.getrefcount(A))
obj2=A()
print("객체 A : ", sys.getrefcount(A))
