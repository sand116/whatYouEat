from flask import Flask, render_template, redirect, url_for, session, request, jsonify, make_response
from service.controller import bp_user as app
# 디비
from service.model import dbHelper
from service import config

# 라우팅
# ~user
# 홈페이지


#로그인
# ~/user/login
@app.route('/login', methods=['POST','GET'])   
def login():
    if request.method == 'GET':
        # 쿠키 획득
        uid = request.cookies.get('uid')
        # 최초에 쿠키가 없으면 uid값에 none뜨는걸 방지해줌.
        if not uid:
            uid =''
        config.cookie_uid = uid
        return render_template('login.html', config=config)
    else:
        uid = request.form['uid']
        upw = request.form['upw']
        row = dbHelper.loginSql(uid,upw)
        #row가 있다면 =>회원이라면 첫번째 조건으로 ㄱ ㄱ
        if row: 
            #세션 처리 (필요한 정보를 세션으로 저장한다)
            session['uid'] = uid
            session['name'] = row['name']
            return redirect(url_for('homebp.main'))
        else:
            return render_template('alert2.html', msg='회원이 아닙니다')

#로그아웃
#~/user/logout
@app.route('/logout')
def logout():
    if not 'uid' in session: # 세션이 없으면~
        # 앞의 config는 클래스에서 정의한 config임.
        return redirect(url_for('userbp.login')) 
    # 세션 종료
    print( session )
    if 'uid' in session:
        session.pop('uid', None)
    if 'name' in session:
        session.pop('name', None)
    print('세션제거후->', session)
        # 페이지 요청을 리다이렉트
    return redirect( url_for('userbp.home'))


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
