numbers=[ i for i in range(1,11) if i%2==0 ] #리스트 표현 식 : for문 -> if문 -> 출력의 순서로 구성
print(numbers)

b=[]
for i in range(1,11) :
    if i%2==0 :
        b.append(i)
print(b)