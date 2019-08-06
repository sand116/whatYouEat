# 파이썬 기초 순서
"""
4. 게임 제작
-> 게임을 만들어 가면서 조건문, 반복문, 식(비교식) 확인
-> 0 부터 99까지의 숫자를 맞추는 게임

step 0:  :게임의 이름을 입력하세요" 코멘트가 나오고
-> step 1: 게임 시작하면 코멘트 안내 하고 입력 유도
===========================================
= enjoy number matching game =
=           v1.0.0           =
==============================
게이머의 이름을 입력하세요 

step 2: 
-> 게임이 사작하면 ai가 숫자를 하나 생성한다
-> 유저는 게임을 시작할 때 이름을 넣고 플레이를 시작하며 숫자를 입력하여 맞추기를 시작한다
   이름을 넣지 않으면 뭐라하고 다시 입력 유도
   숫자를 잘못 넣으면 뭐라하고 다시 입력 유도
-> ai의 숫자보다 유저가 입력한 숫자가 크거나 작으면 코멘트를 해준다
-> 최종 숫자를 맞출때까지 시도 횟수를 기록하며 최종 맞추면
-> 적절한 축하 코멘트 + 시도 횟수를 보여주고 +100-시도횟수*10점을 보상으로 부여하여 보여준다
-> 끝나면 다시 게임할 것인지 물어보고 동의하면 다시 게임 시작
"""

# input이라는 함수는 콘솔에서 사용자의 입력을 대기하다가 사용자가 입력 후 엔터치면 반환하는 함수

#절차적 프로그래밍 


#step 0 입력된 게임 제목의 길이가 33보다 더 크면 다시 입력
while True:
    print("="*50)
    gameTitle=input("게임의 제목을 입력하세요").strip()
    #공백 입력되었을 때도 none으로 받기 위해 strip 공백 없애기
    if len(gameTitle)>33 :
        print('''
        입력하신 게임 제목은 '%s' ,게임 제목은 최대 28(현재 %s자 입력)자를 초과할 수 없습니다.
        다시 입력하세요'''%(gameTitle,len(gameTitle)))
    elif not gameTitle :
        print("다시 입력해주세요\n")
    #파이썬의 블러 특징 : 빈 값이면 false 값  
    else :
        break


#step1: 여러줄 문자열, 포멧팅, 치환식

introComment="""
=====================================
= {0:^33} =
=             v1.0.0                =
=====================================     
""" .format(gameTitle)
print(introComment.strip())

#step2 : 게이머의 이름을 입력받는다
nameCheck= True
#맨 앞줄에 변수 선언하면 전역, if나 while 안에 들어가면 지역
while nameCheck :     
    a=input("게이머의 이름을 입력하세요").strip()
    if not a :
         # 이름을 입력하지 않았다 not a=True
        print("다시 입력받으세요")
        continue
    nameCheck=False
    #break
print("사용자 입력값 : ",a)
print("="*50)
#step 3 : 게임 방식 간단히 설명하고, 0부터 99까지 값을 입력하라고 코멘트
# 아무것도 안 넣으면 뭐라하고, 0이하 99이상 넣어도 뭐라 해야함
print("1:99사이에 값을 입력하시면 ai가 생성한 수와 같은 수를 입력하실 때 정답입니다.")
print("-"*50)


#step 4 : ai가 숫자 하나를 랜덤으로 생성한다. 범위는 0~99 까지
isGamePlaying=True
while isGamePlaying :
    import random as r# 별칭-이름이 길어서
    com_value=None
    i=0 #숫자 맞추기 시도 횟수
    while True :
        #사용자 출력값을 입력받는다
        while True : 
            try:
                num=input(" 0부터 99 사이의 값으로만 ai값을 예측하여 입력하세요\n").strip()
                if not num : #공백을 넣으면
                    print("올바른 입력 값이 아닙니다")
                    continue
                elif num.isalpha() and not num.isdemical() : 
                    # 문자열 함수로, 숫자를 입력하지 않은경우
                    print("숫자가 아닙니다")
                    continue
                #else :
                #   print("ok")
                #정수 변환
                num=int(num)
                # 0 이상 100보다 작고
                if num < 0 or num >= 100 : 
                    print("범위 넘었으니 다시 입력하세요")
                    continue
            except Exception as e:
                print("오류발생",e)
                continue
            break

        #step 4 : ai가 숫자 하나를 랜덤으로 생성한다. 범위는 0~99 까지
        import random as r# 별칭-이름이 길어서
        if not com_value : #값이 없는 경우
            com_value=r.randint(0,99)
        
        i+=1 #파이썬은 ++이 없음
        #step 5 :ai의 숫자보다 유저가 입력한 숫자가 크거나 작으면 코멘트를 해준다- 맞출때까지 반복
        if num > com_value :
            print("-"*50)
            print("AI 값보다 큽니다.더 작은 값을 입력하세요")
            print("-"*50)
            continue
        elif num < com_value :
            print("-"*50)
            print("AI값보다 작습니다. 더 큰 값을 입력하세요")
            print("-"*50)
            continue
        else :
            print("="*50)
            print('''
            정답입니다. 축하합니다.\n
            당신의 정답 : {0}
            ai의 정답 : {1}\n
            {name}의 시도 횟수는 {count},
            당신의 점수는 {point}'''.format(num,com_value,name=a,count=i,point=100-i*10))
            print("="*50)
            break
            
    while True :
        res = input("다시 게임을 할까요? (yes/no)").strip().upper()
        #yes : Yes, YES, yES -->대문자로만 혹은 소문자로만 체크해야함
        if(res == 'YES') :
            break; 
        elif(res == 'NO') :
            isGamePlaying=False
            break

        else : print("정확하게 (yes/no)로 입력하세요")

print("game over~ bye^^")
#step 6: # 적절한 축하 코멘트 + 시도 횟수를 보여주고 +100-시도횟수*10점을 보상으로 부여하여 보여준다
#  끝나면 다시 게임할 것인지 물어보고 동의하면 다시 게임 시작
