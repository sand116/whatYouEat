from flask import Flask, render_template, redirect, url_for, session, request, jsonify, make_response
# 환경 설정 클래스 모듈 가져오기
from service.config import WebConfig
# from service.model.dbMgr import loginsql, searchSql, selectAllEplList
# from service.model.dbMgr import DBHelper
from service.model import createDBHelper

config = WebConfig()
# dbHelper = None

def not_found(error):
    return '404 error %s' % error
def server_error(error):
    return '500 error %s' % error

def create_app(config_path='resource/config.cfg'):
    app = Flask(__name__)
    # 세션 생성에 필요한 세션키(중복되지 않는 해쉬값)를 정의
    app.secret_key = 'slfjwfjskdjfkdfjasd'
    # 환경변수 로드 (파일에서, 객체에서)
    app.config.from_pyfile(config_path, silent=True)
    from service.config import FlaskConfig
    app.config.from_object(FlaskConfig)
    print( '환경변수 사용-->', app.config['DB_URL'] )

    # 디비 로드 -> 웹서비스든 어플리케이션서버든 ->요청할 때마다
    # 디비에 접속->쿼리->닫기 이렇게 작업하지 않는다!!
    # 동접이 천단위로 가면 -> 서비스가 셧다운됨. 혹은 응답이 느리다.
    # 풀링 기술을 이용하여 디비 커넥션, 연결 닫음 미리 준비해둔다.
    # 요청 -> 커넥션 빌림 -> 쿼리 -> 반납 -> 응답
    # 접속과 닫기라는 시간이 세이브가 됨
    #dbHelper = DBHelper(app)
    createDBHelper( app )
    # Flask 객체가 생성된 이후에 라우트 진행되어야 한다.
    # 회원쪽 URL: ~/users/login, ~/users/logout
    # epl URL : ~/epl/allList, ~/epl/search
    # URL에 prefix 부여하여 업무를 분할하고 api 분류할 수 있는 방식
    # blueprint
    from service.controller import user, search, home, my
    from service.controller import bp_user, bp_search, bp_home,bp_my
    app.register_blueprint(bp_user, url_prefix='/user')
    app.register_blueprint(bp_search, url_prefix='/search')
    app.register_blueprint(bp_home, url_prefix='/')
    app.register_blueprint(bp_my, url_prefix='/my')

    app.register_error_handler(404, not_found)
    app.register_error_handler(500, server_error)
    initRoute(app)
    # 에러 핸들러 등록
    return app

# 모든 페이지에서 적용되는 공통사항
def initRoute(app):
    # 요청과 응답 전후로 이런 이벤트를 감지하여 전처리, 후처리를 수행하는
    # 이미 정해져 있는 함수들
    @app.before_first_request
    def before_first_request():
        print('서버가 가동하고 최초 요청시 반응 단 한번')

    @app.before_request
    def before_request():
        # 세션이 없는 경우

        # if request.url.find('/static')>=0:
        #     print('정적 경로는 모두 패스')
        # # elif not 'uid' in session : 
        # #     if request.url.find('/login')<0 and request.url.find('/signup')<0 :
        # #         return redirect(url_for('homebp.index'))
        # # print(request.url,'uid' in session )
        print('요청 할 때마다 무조건 여기를 거친다: 전처리')

    @app.after_request
    def after_request( res ):
        print('매번 요청 처리되고 나서 실행됨, 응답이 지나가는 곳')
        return res

    @app.teardown_request
    def teardown_request(exception):
        print('브라우저가 응답하고 나서 실행')
        return '브라우저가 응답하고 나서 실행'

    @app.teardown_appcontext
    def teardown_appcontext(exception):
        print('http 요청 어플리케이션 컨텍스트 종료되고 실행')


# 환경 변수 체크하는 곳
# configCheckTest( app.config.items())
def configCheckTest(config):
    for key, value in app.config.items():
        print(' %s: %s ' % (key, value) )


# 스타트 파이로 넘어감.
#if __name__ == '__main__':
#    app.run(debug=config.debug)