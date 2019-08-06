
####################################################
#클라이언트가 웹페이지를 요청할 때 데이터를 보내고 싶다
# 데이터를 보내는 방법 : method(get, post,...), 동적 파라미터
#페이지를 요청할 때 데이터 보내기 : method 방식
# get : url?uid=ppp&age=10 (key=값)
# uid,age 등은  키 값 &는 (키=값) 세트를 연결하는 구분자
# 문제점 : 데이터가 눈에 보인다 --> 보안에 취약하다 , 대용량 데이터 , 큰 데이터는 전송 불가 -> 짤림
# 왜-->(http 프로토콜의  헤더(머리)의 데이터를 세팅해서 전달하기 때문에 공간이 적다.)
# 장점 : 구성이 편하고, 전달도 빠르다.(상대적)



#1. 모듈 가져오기
from flask import Flask,request, render_template
 #flask 모듈로부터 flask 클래스를 가져옴 - pip install flask 로 설치
#pip list - 설치된 모듈 확인




  
# 1. 모듈 가져오기
#2. 앱 생성(서버 생성)
app = Flask(__name__)

# 3. 라우팅(요청을 분석하여 어떤 함수가 응답할지 매칭해주는 것)
# 요청 : http +:// + 아이피 + : +포트+/+세부페이지이동

# @app.route('/') #요청
# #아무런 세팅이 없으면 기본 get 방식으로 요청함을 의미한다.
# def home() : #응답함수
#     #return 'home page'


#     #html 은 응답 데이터의 뼈대 및 콘텐츠 담당
#     #css는 스타일, 레이아웃, 디자인 담당
#     #javascript(js) 는 사용자의 인터렉션, 이벤트 담당
#     return "<h1 style='color:red;background:black'>home page</hi>"
    

# /login 이라는 요청을 처리하는 웹서비스를 구성하시오


# @app.route('/login')
# def login() :
#     return "login page"

 #/logout 구현   
@app.route('/logout2')
def logout( ):
    return ("logout")

#http://127.0.0.1:5000/users/login을 처리할 페이지를 구성해라
#세부 요청페이지를 어떤 함수가 처리할것인지 매칭하는 기능
#라우트->라우팅
# @app.route('/users/login') #페이지 주소(URL) 정의
# def login() :
#     return "로그인 page"

#동적 파라미터 1 ->url(주소)에 데이터를 보내는 방법
@app.route('/news/<news_id>') #<url이름>- 데이터가 이것을 타고 옴
def news(news_id) :
    return "전달된 데이터 %s"%news_id

#전달된 데이터 보이면 안되는 것 - 아이디, 비번 등 이런 데이터는 전달하면 안된다 ->보안에 취약하다
# @app.route('/login/<uid>/<upw>') #주소에 데이터를 넣어서 서버에 전달
# def login(uid,upw) :
#     return '%s %s' %(uid,upw)

#동적 파라미터 2 : 타입을 지정하여 보다 명확하게 데이터를 전달할 수 있다.
#타입 : int,float(부동소수, 소수), path(가변경로)
@app.route('/test/<int:num>') #flask에서는 이렇게 정의한다
def test(num) :
    return '정수형 전달 데이터 %s' %num

@app.route('/test2/<int:num>') #flask에서는 이렇게 정의한다
def test2(num) :
    return '전달 데이터 %s' %num

@app.route('/test3/<path:num>') # path 뒤에는 한덩어리로 인식 -자유도
def test3(num) :
     #전달 데이터 분해해서 표시하기
    a=num.split("/") #결과값 리스트
    return '전달 데이터 %s' %a
##################################################################

@app.route('/')
def home() :
    print('1')
    # get 방식을 통해서 전달될 데이터를 뽑을려면 -->request 객체 
    # return 'homepage %s'% request.method
    return  render_template('login.html', name='멀티')#키=값
  #->html을 랜더링하여 뿌려준다 - 보여주고자 하는 html 파일을 만들어서 templates 폴더 밑에 위치시키고
    #render_template('html 파일명)



@app.route('/login') #이 아이를 갈 때 데이터 전달
def login():
    # request.args.get("키")
    uid=request.args.get('uid') #키 값이 uid인 전달되는 데이터를 획득해서 변수에 담기
    upw=request.args.get('upw')
        # return ' %s,%s' %(uid,upw) #request 요청할때 담는 그릇 
 

# 위의 식의 결과 : http://127.0.0.1:5000/uid=ppp&age=10로 요청
 #이건 html 언어는 파이썬 안에서는 의미가 없는 그냥 텍스트인데, 이게 웹브라우저에서 들어가면 html문서가 해석됨 -브라우저 랜더링(html로 짜여진 것만)

    #디비(저장소) 에 쿼리했다 치고
    if uid=='test' and upw=='1234' :
        return "회원입니다"
    else : return '''
        <script>
        alert("%s"); //팝업 띄우기
        history.back(); // 이전 페이지로 이동
        </script>
       ''' %'일치하는 회원정보가 없습니다. 가입하시겠습니까' #파이썬은 무엇을 리턴했다는 것은 중요하지않음 파이썬 입장에서는 그냥 텍스트 리턴
# 4. 서버 가동
if __name__ =="__main__" : #main이 될때만 서버 작동
    # 디버깅 모드를 사용하면 내가 수정한 내용이 반영되어 자동으로 재가동됨 -> 즉 자동반영된다.
    #초기값이 설정되어있지 않다는 것은 기본설정값이 False 라는 것이기 때문에 debug를 True로 바꿔줌
    # app.run(debug=True)
    # 서버주소는 ip와 포트주소로 구성 : 기본 포트는 5000번을 사용하는데 통상 80번은 생략 가능
    # 포트란?  http://127.0.0.1:5000/ 포트는 기본 아이피에서 0~65535개 포트를 사용할 수있음
    # 같은 ip주소(장비)에 할당되는 수십개의 프로그램이 구동되기 위해  
    app.run(debug=True)
else :
    print("본 모듈은 단독으로 구동될때만 정상 작동합니다.")