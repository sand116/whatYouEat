
class Person2: 
    ''' 
    멤버 변수 : 객체의 속성을 대변
    '''
    name = None
    age = 0
    '''
    멤버 함수 : 객체의 행동(액션)
    '''
    def eat(self):
        print ('eat() call')
    def sleeping(self):
        print ('sleeping() call')
    #생성자의 주업무 중 하나는 멤버 변수 초기화에 있다.
    def __init__(self,name,age): #멤버 변수 초기화를 위해
        #클래스 내부에서 멤버들을 사용할 경우 무조건 self.을 붙인다.
        #self는 자기 자신 class를 가지는 키워드
        self.name=name #self.name(내 멤버변수에다가 name이라는 지역변수를 넣어줄거야)
        self.age= age
        print("생성자 call")

p1=Person2('박진경',25) # inint 함수 인자값으로 가서 박진경, 25로 초기화
p2=Person2('한준모',25)

#이름을 출력하시오
print(p1.name)
print(p2.name)

#############################################
# xMan 정의한다
# xMan은 Person2를 상속받는다-> 즉, xMan은 Person2이다
# Person2는 Xman이다 :Person2는 xMan을 자식으로 가진다
# dog은 동물이다 but 동물이 dog는 아님
#동물은 dog이다 -> 동물은 dog를 자식으로 가진다 : has a
#############################################

#class 클래스명(부모) : ->상속을 표현
#부모가 object인 경우 생략 가능
#class Person2(object)
#class Person2(object) or class Person2

#상속을 받으면 부모의 모든 것을 다 사용할 수 있다 - 부모의 멤버 함수, 멤버 변수 다 사용 가능
#자식은 별도로 변수나 함수를 추가할 수 있다.
#자식은 물려받은 부모이ㅡ 것을 재정의(업그레이드) 할 수 있다.
class XMan(Person2) :
    abil=100
    def speed(self) :
        print("시속 200km로 달린다")
    def eat(self) :
        print("밥을 1초만에 다 먹을 수 있다")
        #부모로부터 받은 함수를 재정의하여 사요야
        
    def __init__(self,name,age) : #부모가 갖고있으니깐 가지고 있음
        self.name=name
        self.age=age

xman=XMan('장영환',25)
print(xman.name,xman.abil)


# print('__name__의 내용은 %s'% __name__)
# __name__ 이 p1_mod이고 이는 지금 메인임

if __name__=="__main__" :
    # p1_mod.py 가 실행 메인 코드가 돼서 구현될때
    # 모듈로 사용되면 이부분은 수행되지 않는다.
    #모듈로 사용될 경우 수행됮 않고, 메인으로 구동될 때만 수행될 코드를 기입
    #일반적으로는 테스트 코드 사용 (모듈 용도로만 사용되면)
    p1=Person2('박진경',25) # inint 함수 인자값으로 가서 박진경, 25로 초기화
    p2=Person2('한준모',25)

    #이름을 출력하시오
    print(p1.name)
    print(p2.name)
    xman=XMan('장영환',25)
    print(xman.name,xman.abil)
        
        