
from flask import Flask 

app = Flask(__name__)
# 데코레이터는 하나의 함수에 여러개를 연결할 수 있다.
# 데코레이터는 하나의 함수에 여러개를 연결할 수 있다.
#  @ : 데코레이터
@app.route('/test') #내부적으로 이렇게 호출 : home()
@app.route('/test/<id>') # 내부적으로 이렇게 호출 : home('pp')
def home(id=None) : #함수 하나가 두가지 url 동시 처리  -기본 값 처리를 하면 
    if id : 
        return "sub page %s"%id
    else :
        return "home page

if __name__ =="__main__" :
    app.run(debug=True)

    for i in range(1,5) :
        print(i)