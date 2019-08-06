from flask import Flask,render_template,redirect,url_for,session, request, jsonify, make_response
from service.config import WebConfig
# from service.model.dbMgr import loginSql,searchSql,selectAllEplList
#from service.model.dbMgr import DBHelper
from service.model import createDBhelper


config=WebConfig()
#dbHelper=None
#환경설정 클래스 모듈 가져오기

def not_found(error):
    return '404 error %s' % error
def server_error(error):
    return '500 error %s' % error
def create_app(config_path='resource/config.cfg'):
    app = Flask(__name__)
    app.secret_key='iloveyou'
     # 앱 만들기
     # 환경변수 로드( 파일에서, 클래스에서 )
    app.config.from_pyfile(config_path, silent=True)
    # 프로그램에서 사용되는 고정된 정보(디비접속,운용수치 등)은 외부파일에서 관리하는 것이 일반적(소스에 고정하지않음)
    #통상 상수값임(변수명 대문자)
    # #파일에서 환경변수(정적인 것) 로드

    from service.config import FlaskConfig
    app.config.from_object(FlaskConfig) #클래스 모듈 가져오기
   
    print('환경변수 사용->', app.config['DB_URL'])
     # 디비 로드
     # flask 객체가 생성된 이후에 라우트 진행
    #환경변수 체크하는 함수 
    print('현재까지 환경변수 확인')
    configCheckTest(app.config.items())
    ###########################################################################
    #디비 로드 ->웹서비스든 어플리케이션서버든 ->요청할 때마다 디비에 접속->쿼리->닫기 이렇게
    #작업하지 않는다!
    #위와 같이되면, 동접(동시접속)이 천 단위로 가면 서비스가 셛다운됨, 살아도 응답이 느리다.
    ################################################################################
    #풀링(커넥션 풀)이라는 기술을 이용하여 디비 커넥션, 연결닫음 미리 준비해둔다.
    #요청 ->커넥션 빌림-> 쿼리 ->반납 ->응답 : 접속과 닫기 시간이 save가 됨
  
    createDBhelper(app)

      #dbHelper=DBHelper(app)
      #Flask 객체가 생성된 이후에 라우트 진행되어야 한다
      #회원 쪽 URL : ~users/login, ~/users/logout, ~/users/join
      #epl URL : ~epl/allList,~epl/search,
      # url에 prefix를 부여하여 업무를 분할하고 api를 분류할 수 있는 방식
      # 블루프린트(blueprint)
    from service.controller import bp_user,bp_epl,bp_bbs,bp_home
    from service.controller import user,epl,bbs,home
    app.register_blueprint(bp_user,url_prefix='/user')
    app.register_blueprint(bp_epl,url_prefix='/epl')
    app.register_blueprint(bp_bbs,url_prefix='/bbs')
    app.register_blueprint(bp_home, url_prefix='/')
    initRoute(app)

    app.register_error_handler(404, not_found)
    app.register_error_handler(500, server_error)
    initRoute(app)
    # 에러 핸들러 등록
    return app
    #items()는 함수
   

################################################################################

def initRoute(app) :
    #요청과 응답 전후로 이런 이벤트를 감지하여 전처리, 후처리
    #를 수행하는 이미 정해져있는 함수들 
    @app.before_first_request
    def before_first_request() :
        print("서버가 가동하고 최초 요청시 반응 단 한 번")
    @app.before_request #모든 요청이 거쳐야하는 관문
    def before_request():
        print("요청 직전")
        if not 'uid' in session : 
            if request.url.find('/login')<0 and request.url.find('/signup')<0 :
                return redirect(url_for('userbp.login'))

        #세션이 없는 경우
        # print(request.url, 'user_id' in session ) # session이 있는지 확인하는 조건문
        # print("요청할 때마다 무조건 여기를 거친다 : 전처리")


    @app.after_request
    def after_request(res) : #res:응답
        #print("매 요청 처리되고나서 실행됨, 응답이 지나가는 곳")
        return res
    
    @app.teardown_request
    def teardown_request(exception) :
        #print("브라우저가 응답하고 나서 실행")
        return '브라우저가 응답하고 나서 실행'

    @app.teardown_appcontext
    def teardown_appcontext(exception) :
        print("http 요청 어플리케이션 컨택스트 종료되고 실행")

def configCheckTest(config) :
    for key,value in config :
        print("%s : %s" %(key,value))

