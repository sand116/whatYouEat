from flask import Flask,render_template,redirect,url_for,session, request, jsonify, make_response
from service.controller import bp_user as app
#디비
from service.model import dbHelper #객체 변수 땡겨옴
from service import config

#라우팅


#~/url/login ->url_for로 구현되기때문에 굳이 이렇게 url이 바뀌어도 괜찮게 됨..!!!
@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='GET':
        #쿠키 획득 : get방식일때 
        uid=request.cookies.get('uid')
        #uid아이디를 쿠키로 받음
        #쿠키가 없을 경우 : None으로 나오기 때문에 기본값 처리 
        if not uid: #uid==None
            uid=''
        config.cookie_uid=uid
        return render_template('login.html',config=config)
    else :
        uid=request.form['uid'] #post 방식으로 요청
        upw=request.form['upw']
        row=dbHelper.loginSql(uid=uid,upw=upw) #디비쿼리수행
        # false :[],(),{},0,""
        # row ->dit =>{..}
        # row에 uid upw name 저장
        if row :
            #세션처리(필요한 정보를 세션으로 저장한다) -서버 메모리에 저장
            session['uid']= uid
            session['name']=row['name']
            #세션종료
            return redirect(url_for('userbp.home'))
        else :
            return render_template('common/alert.2.html',msg='회원이 아닙니다')
            
    #경고창 ->되돌아가기

#로그아웃
#~/user/logout
@app.route('/logout')
def logout():
    if not 'uid' in session :
        return redirect(url_for('userbp.login'))
    #세션 종료
    print(session)
    if 'uid' in session:
        session.pop('uid',None)
    if 'name' in session:
        session.pop('name',None)
        print("*"*50)
    print('세션제거후 :',session)
    #페이지 요청을 리다이렉트 ->홈페이지
    return redirect(url_for('userbp.home'))
    # 세션없으면 로그인 서버로 가서, get방식으로 로그인 페이지 호출 post방식이면 로그인서버로 들어가고

# 회원가입-> 디비에 추가 ->세션권한을 줘서 홈에 들어갈수 있게해야함
@app.route('/signup',methods=['GET','POST'])
def signup() :
    if  request.method=='GET' :
        # return render_template('firstpage.html',config=config)
        return render_template('signup.html',config=config)
    else :
        uid=request.form['uid']
        upw=request.form['upw']
        name=request.form['name']
        row=dbHelper.signupSql(uid=uid,upw=upw,name=name)
        
        return render_template("common/alert.2.html", msg="등록 성공")
          