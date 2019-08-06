from flask import Flask,render_template,redirect,url_for,session, request, jsonify, make_response
from service.controller import bp_user as app
#디비
from service.model import dbHelper #객체 변수 땡겨옴
from service import config

#라우팅
@app.route('/')
def home() :
    #세션이 없으면 /login으로 리다이렉트 
    # 만약 이 서버에 접속하는 사람이 2명이상일때도 이 조건문이 성립하는가?
    # if not 'uid' in session :
    #     return redirect(url_for('login'))

    ################################################
    # 쿠키 적용 : 응답을 이용 - 사용자의 브라우저에다가 특정정보를 남기는 것
    # ->아이디를 저장해서 로그인페이지 뜰때 자동으로 아이디가 보이게 하기.
    # 응답 객체를 생성한다.

    # 쿠키 세팅
    resp=make_response(render_template('index.html',config=config)) #render template 반환할때 쿠키 세팅해서 응답하기.
    resp.set_cookie('uid', session['uid'])
    return resp

#~/url/login ->url_for로 구현되기때문에 굳이 이렇게 url이 바뀌어도 괜찮게 됨..!!!
@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='GET':
        #쿠키 획득 : get방식일때 
        uid=request.cookies.get('uid')
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