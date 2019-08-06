#연속 데이터
print('='*70)
nums=None #값이 없기 때문에 타입이 없다 NULL대신 사용

#비어있는 리스트 생성
nums=[]
print(nums,len(nums),type(nums))

#0보다 크고  10보다 작은 정수들 중에 홀수만 멤버인 리스트를 생성
nums=[1,3,5,7,9]
print(nums,len(nums),type(nums))
anis=['dog','cat','bird']
print(anis,len(anis),type(anis))
#리스트의 멤버들의 타입이 동일할 필요는 없다
mix=[1,2,3,'dog','cat']
print(mix,len(mix),type(mix))
#차원을 뒤섞으면?
multimatrix=[1,2,3,['dog', 10]]
print(nums,len(nums),type(nums))
print(multimatrix,len(multimatrix),type(multimatrix))

#======================================================
#mix 라는 리스트에서 3을 출력하시오->리스트 인덱싱
print(multimatrix[2])
#multimatrix에서 dog를 출력하시오
print(multimatrix[3][0])

#슬라이싱
nums=[1,3,5,7,9]
#nums 리스트에서 3,5,7,만 멤버로 가진 리스트를 구하시오
print(nums[1:-1])
#프린트는 사본작업이고 원본은 변화하지 않음
print(nums)
#특정 멤버 변경 
nums[0]=100
print(nums)
print(nums)
#3,5,7을 전부 -1로 변경하시오  - 슬라이싱도니 리스트 값을 대입할 경우에는 하나의 값이 아닌 연속값 형태로 대입해야함
nums[1:4]=[-1,-1,-1] #연속데이터여야지만 대체가 가능하다는 것이 본질!
nums[1:4]='-1'# 슬라이싱 한 값은 연속데이터고 연속데이터여야 한다는 것이 본질이므로, 개수는 상관이 없음 
print(nums)

#내장함수 - del 정의한 것 삭제
del nums[0] 
del nums[:2]
print (nums)
#리스트 함수
nums.remove(9) #인덱스가 아니라 값을 삭제
# 다제거
nums.clear()
#추가 정렬
nums.append(100)
print(nums)
nums=[4,2,3,5,5,67,2,22,34,3]
nums.sort() #원본 조작
print(nums)

#원본은 훼손하지 않고 오름 차순 정렬하여 마지막 값을 출력하시오
nums=[3,4,2,7,8,3,1,89,6]
print(nums[:])
nums2=nums[:] #nums[:] - 사본 획득->정렬 ->데이터출력
nums2.sort()
print(nums2[-1])
print('원본확인',nums)

#리스트 연산
print(nums+[1]) # 뒤에 1 추가 - 같은 리스트 형태면 연산 가능

#값을 넣어주는 행위나 리스트 자체에 함수를 적용하는 경우 리스트 원본 훼손 : 단순 슬라이싱하는 행위,인덱싱 자체는 원본 훼손하지않음 
#========================================================
# 연속데이터 (컬렉션, 시퀀스 데이터) 여러개 데이터를 하나의 이름 (변수명) 으로 관리하고 프로그램을 좀더 
# 편하게 구성하기 위해서 나온 방식
