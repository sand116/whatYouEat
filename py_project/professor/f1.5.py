# 페이지를 요청할때 데이터 보내기 : method 방식
# get : url?uid=ppp&upw=10
#       uid, age등은 키값
#       & (키=값)세트를 연결하는 구분자 
# 문제점:데이터가 눈에 보인다 => 보안에 취약하다, 
#        큰데이터는 전송불가=> 짤림 => 왜?(http 프로토콜의 
#        헤더(머리)에 데이터를 세팅해서 전달하기때문에
#        공간이 적다
# 장점 : 구성이 편하고, 전달도 빠르다(상대적)
# 1. 모듈 가져오기
from flask import Flask, request

# 2. 앱생성(서버생성)
app = Flask(__name__)

# 3. 라우팅(요청을 분석하여 어떤 함수가 응답할지 매칭)
# 아무런 세팅이 없으면 기본 get 방식으로 요청함을 의미한다
# http://127.0.0.1:5000/uid=ppp&age=10
@app.route('/')
def home():
    # get방식을 통해서 전달될 데이터를 뽑을려면 => request 객체
    #return 'home page %s' % request.method
    return '''
        <!-- html : hyper text markup language -->
        <html>
            <head>
                <!-- html 문서의 메타 정보를 표현하는 위치 -->
            </head>
            <body>
                <!-- 눈에 모이는 모든 부분 -->
                <!-- 사용자로부터 아이디와 비번 입력받아라
                    로그인 버튼을 누르면 로그인 처리하는 페이지로
                    아이디와 비번을 가지고 요청한다
                    -> 해당 페이지는 아이디 비번 가지고 디비에 쿼리
                    -> 쿼리 결과 회원이면 -> 정상 처리(서비스이동)
                    -> 회원아니면 메시지 처리(가입,재로그인 유도)
                -->
                <fieldset>
                    <form action='/login' method='get'>
                        <input type='text' name='uid' placeholder="아이디" autofocus required/>
                        <br/>
                        <input type='password' name='upw' placeholder="비밀번호" required/>
                        <br/>
                        <input type='submit' value='로그인'/>
                    </form>
                </fieldset>
            </body>
        </html>
    '''
# http://127.0.0.1:5000/login?uid=ppppppp&upw=1111111
@app.route('/login')
def login():
    # request.args.get('키')
    # 전달될 데이터 획득해서 변수 담기
    uid = request.args.get('uid')
    upw = request.args.get('upw')
    #return 'uid:%s upw:%s' % (,)
    # 디비에 쿼리했다치고
    if uid=='test' and upw=='1234':
        return '회원입니다'
    else:
        return '''
        <script>
            alert("%s");    // 팝업 띠우기
            history.back(); // 이전 페이지 이동
        </script>
        ''' % '일치하는 회원정보가 없습니다. 가입하겠...'

# 4. 서버 가동
if __name__ == '__main__':
    app.run(debug=True)
else:
    print('본 모듈은 단독으로 구동될때만 정상 작동합니다.')