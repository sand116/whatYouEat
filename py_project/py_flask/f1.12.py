#url_for
#flask 내부에서 URL을 직접 입력하지 않고, url_for(라우팅된 함수명) 처리
# 주소가 변경되고 , 소스레벨에서 수정될 내용이 없다
from flask import Flask,url_for
app=Flask(__name__)
        
@app.route('/') 
def home() : pass     

#get방식이면서, 동적 파라미터
@app.route('/users/<uid>') 
def users(uid) : pass   

@app.route('/join/<uid>',methods=['POST']) 
def join(uid) : pass  

#get,post,put 방식이면서 -> restful, 동적 파라미터
@app.route('/join2/<uid>', methods=['GET','POST','PUT'])
def join2(uid) : pass 
       

# URL 테스트
# 파이썬 내부에서 URL을 문자열로 기술시 url_for('함수명') 이용하여 처리
with app.test_request_context() :
    print("홈페이지 즉 /=>", url_for('home')) 
    print("동적파라미터 즉 /=>", url_for('users',uid='유저아이디'))
    #유저 아이디가 %EC%9C%A0%EC%A0%80%EC%95%84%EC%9D%B4%EB%94%94 로 되는 것은 
    #url 인ㅋ코딩이 되어서 한글이 깨지거나, 문자 깨짐을 알아서 방지해 주는 것


if __name__ =="__main__" :
    app.run(debug=True)
