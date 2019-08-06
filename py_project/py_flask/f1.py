#1. 모듈 가져오기
from flask import Flask #flask 모듈로부터 flask 클래스를 가져옴 - pip install flask 로 설치
#pip list - 설치된 모듈 확인 

#2. 앱 생성(서버 생성)
app = Flask(__name__)

# 3. 라우팅(요청을 분석하여 어떤 함수가 응답할지 매칭해주는 것)
@app.route('/')
def home() :
    return "home page"

# 4. 서버 가동
if __name__ =="__main__" :
    app.run()