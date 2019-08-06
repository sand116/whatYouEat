# # 함수 :function <-> 메쏘드(method)
# # 왜 ? : 반복작업 해소 -> 생산성, 개발속도, 재사용성 향상
# # [..]-->생략 가능하다!
# # def 함수명 ([인자이름])
# # 함수 내부에서 할 일 기술
# # [return 결과값]
# a=1
# b=2

# def sum(x, y) : 
#     return x + y

# #함수 호출 -->함수명()
# d=sum(a,b)
# print (d)


# #가변 인자(argument or params) 
# def sum2(*args) :
#     sum=0
#     for n in args :
#         print(n)
#         sum=sum+n
#     return sum
#     #전달된 인자가 모두 정수 값이라면 인자의 총합을 구해서 리턴하시오
# print(sum2(1,2,3,4))

# #주어진 리스트의 모든 멤버의 누적곱을 구하시오
# list=[1,2,3,4]
# def mul(input) :
#     # 중간 중간 계산 값을 담고 있을 변수
#     tmp=1
#     for n in input :
#         tmp=tmp*n
#     return tmp
# print("누적곱 :", mul(list))
# # 주어진 리스트의 모든 멤버의 누적합, 누적곱을 구해서 리턴하시오 ->함수의 리턴값이 2개다

# def mix(input) :
#     s=0 #누적합의 임시 데이터를 담는 변수
#     m=1 #누적곱의 임시 데이터를 담는 변수
#     for n in input :
#         s+=n
#         m*=n
#     return s,m

# print(mix(list))
# t_sum,t_mul=mix(list) #튜플 반환 값을 받아주기.
# print('t_sum=%s, t_mul=%s' %(t_sum,t_mul))

# ##############################################################
# def mixEx(input) :
#     s=0 #누적합의 임시 데이터를 담는 변수
#     m=1 #누적곱의 임시 데이터를 담는 변수
#     for n in input :
#         s+=n
#         m*=n
#     return {'t_sum':s,"t_mul" :m}
# nRtn=mixEx(list)
# print("합",nRtn['t_sum'])
# print("곱",nRtn['t_mul'])

# ################################################################
# #문자열을 입력받아서 공백을 제거하고 리턴해주는 함수를 만드시오
# ###############################################################
#정의
def trim(input) :
    b=input.strip()
    return(b)
#테스트
str=input("입력하세요")
print(trim(str))

#카테고리 df
#사용자 정의 함수 : trim()
#내장 함수 : type(),len()
#멤버 함수 : random.randiant()-->에서 randiant -->누군가의 멤버
################################################################
isTest =True
def log (msg) :
    if isTest :
        print('-'*20)
        print(msg)
        print('-'*20)
log("hello world")

#############################################################
#함수 인자에 초기값 부여하여 활용
def setPerson(name='멀티', age='50', weight=80) :
    log( '이름 =%s 나이= %s 무게= %s'%(name,age,weight))

setPerson('홍길동',100,70)
setPerson('홍길동2',900)
setPerson()
setPerson(weight=100)
a=[15,20,3]
a.sort() #reverse=false였음
a.sort(reverse=False)
print(a)
