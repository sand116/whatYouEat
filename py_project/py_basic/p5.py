'''
1. 연속 데이터 관련 /시퀀스 타입
- 집합 :set(), 중복제거, 순서는 중요하지 않음 
'''
print('='*70)
a ='helloworld'
#a가 가르키는 문자열의 중복 문자 제거
b =set( a )
print(b)
c=list(b) # 리스트 형태로 변환 - 문자열 변환은 str()
print(c)
c.sort() # 알파벳 순 정렬
print(c)
# 원본데이터 -> set()중복제거 ->특정 시퀀스 타입 변화 -> 원하는 업무 진행 

##############################################################
# 합집합, 교집합, 차집합  함수
a=set([1,3,4,5,7,9,2,6,5])
b=set([2,4,6,8,1,5,3,2])
print(a,b)
print(a.union(b)) #합칩합
print(a.intersection(b)) #교집합
#차집합 : 방향에 따라 결과가 다름
print(a.difference(b)) #a-b
print(b.difference(a)) #b-a