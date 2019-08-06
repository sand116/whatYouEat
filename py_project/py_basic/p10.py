#반복문  
a=[1,2,3,4,5]

#리스트 a의 멤버들을 하나씩 꺼내서 출력하시오 

for item in a : 
    print( item) #앞에서부터 차례대로 뽑아냄
# 삭제하는 함수 del(내장) 문자열 함수 - 
a=[(1,2),(3,4),(5,6)]

#튜플의 경우 데이터를 개별적으로 받을 수 있다.
for i,j in a: #튜플 i,j=(,) 알아서 담김 - 변수를 n개로 해서 일일히 받아낼 수 있음
  print (i,j) 
for item in a :
    print( item[0],item[1]) #앞에서부터 차례대로 뽑아냄 
   #튜플 인덱싱

#연속수 ->range()
for n in range(1,11) : # range(x,y) x<=n<y
    print(n)

#출력결과

'''
3단부터 7단까지 출력하시오
'''

for i in range(3,8) :
    for j in range(1,10) :
        print("%s x %s = %10s " %(i,j,i*j))

print("-"*50)
#축약 
#똑같은 결과를 바로 리스트에 
print(["%s x %s = %10s " %(i,j,i*j) for i in range(3,8) for j in range(1,10)])