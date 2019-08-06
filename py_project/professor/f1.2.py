# 1. 모듈 가져오기
from flask import Flask

# 2. 앱생성(서버생성)
app = Flask(__name__)

# 3. 라우팅(요청을 분석하여 어떤 함수가 응답할지 매칭)
@app.route('/')
def home():
    return 'home page'
    # html은 응답 데이터의 뻐대 및 콘텐츠 담당
    # css는 스타일, 레이아웃, 디자인 담당
    # javascript(js)는 사용자의 인터렉션, 이벤트 담당 
    #return '<h1 style="color:red;background:black">home page</h1>'
    #return "<script>alert('hi');</script>"

# 4. 서버 가동
if __name__ == '__main__':
    # 디버깅 모드를 사용하면 내가 수정한 내용이 반영되어 
    # 자동으로 재가동된다 -> 즉 자동반영된다
    # 기본 포트는 5000번을 사용하는데 통상 80번은 생략 가능
    # 포트?(port):포트는 기본 아이피에서 0 ~ 65535:
    # 총 65536개포트를 사용 => 채널을 생각하면 쉬움
    # http://127.0.0.1:5000/
    # app.run(debug=True)
    # or
    app.debug = True
    app.run()
else:
    print('본 모듈은 단독으로 구동될때만 정상 작동합니다.')