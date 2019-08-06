from flask import Flask, render_template, redirect, url_for, session, request, jsonify, make_response
from service.controller import bp_home as app
# 디비
from service.model import dbHelper
from service import config

@app.route('/')
def home():
    resp = make_response(render_template('index.html', config=config) )
    # 쿠키 세팅
    resp.set_cookie('uid', session['uid'])
    return resp


    #세션이 없으면 /login으로 리다이렉트 
    # 만약 이 서버에 접속하는 사람이 2명이상일때도 이 조건문이 성립하는가?
    # if not 'uid' in session :
    #     return redirect(url_for('login'))

    ################################################
    # 쿠키 적용 : 응답을 이용 - 사용자의 브라우저에다가 특정정보를 남기는 것
    # ->아이디를 저장해서 로그인페이지 뜰때 자동으로 아이디가 보이게 하기.
    # 응답 객체를 생성한다.
    # 쿠키 세팅