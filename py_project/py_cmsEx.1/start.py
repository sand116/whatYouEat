from service import create_app, config

#플라스크 어플리케이션 서버 생성
application=create_app()

# 구동
if __name__ =="__main__" :
    # print(application.config['TEST_PORT'])
    # print(application.config['TEST_URL'])
    host=None
    port=None
    if application.config['ENV']=='production' : #상용
        host = application.config['REAL_URL']
        port = application.config['REAL_PORT']
    else : #개발,테스트
        host = application.config['TEST_URL']
        port = application.config['TEST_PORT']

    application.run(
        host=host, #0.0.0.0으로 두면 알아서 서버에서 ip 생성
        port=port,
        debug=application.config['SERVER_RUN_MODE_DEBUG'])
#config 와 model 은  파이썬 패키지 
