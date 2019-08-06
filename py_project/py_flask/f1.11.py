
from flask import Flask,request,render_template, redirect,url_for
from d1_8 import loginSql
app = Flask(__name__)

        
@app.route('/login',methods=['GET','POST'])        
def login() : 
    if request.method == 'GET' : # =route가 요청하는 기본method는 항상 get
        return render_template('login.html',name="multi")
        
    elif request.method=='POST' :
        return loginProcess()  

def loginProcess() :
    uid=request.form['uid'] #post 방식으로 요청
    upw=request.form['upw']
    print(uid,upw) 

    # 디비 쿼리 수행
    rows=loginSql(uid=uid,upw=upw)
    if rows : #rows가 db에서 받아  반환하면
        return redirect(url_for('main')+'?name=%s'%rows[0]['name']) # return '/service'
    #만약 html에서 input하면 위에 처럼 ~/service?name=멀티 헤더로 보내주는 것이기 때문에 위처럼 쓰면
    #get방식으로 보냄을 의미
    #~/service?name=멀티 - 멀티라는 것을 
    else :
        return render_template('alert.2.html',msg='회원이 아닙니다')
    #경고창 ->되돌아가기

@app.route('/service')
def main() :
    return "main page %s"%request.args.get('name')     #~/service?name=멀티로 get방식으로 요청함

if __name__ =="__main__" :
    app.run(debug=True)