a=range(100000000000)
print(a) #range(0,10) 출력
#lazy loading 늦은실행 때문임 - 선언만 되는 것이며, 실제 메모리에 넣어 놓지 않음

print(list(a)) #리스트 함수를 통해서 실행될 때 메모리에 올라옴
for i in a: #실행하는  이럴때만 메모리에 올라옴 
    sum=sum+i
    if i>10 :
        break


# 이때는 다 찍힘