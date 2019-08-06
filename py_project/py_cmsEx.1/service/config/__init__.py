#config는 환경설정이라는 말 - 모든 것에 공통되는 사항을 저장해놓음
class FlaskConfig(object) :
    DB_URL         ='localhost' #127.0.0.1와 같음
    DB_PORT        =3306
    DB_USER        ='root'
    DB_PASSWORD    ='811201'
    DB_DATABASE    ='pythondb'
    DB_CHARSET     ='utf8'
    MAX_POOL       =    100 #디비 커넥션 연결 수
class WebConfig :
    #멤버변수
    title       ='cms'
    site_name   ='Flask 기반 콘텐츠 관리 시스템'
    version     ='v1.0.0'
    debug       = True
    page_title  ={'LOGIN' : '관리자 로그인','MENU1':'2017~2018 EplList'}
    cookie_uid  = None

    #멤버함수
    #생성자
    def __init__(self):
        print("환경설정 생성자 호출")
        
if __name__=='__main__' :
    obj=WebConfig()
    print(obj.site_name)