from flask import Flask, render_template, redirect, url_for, session, request, jsonify, make_response
from service.controller import bp_home as app
# 디비
from service.model import dbHelper
from service import config

@app.route('/')
def index():
    return render_template('index.html', config=config)
    # 쿠키 세팅
   
@app.route('/main')
def main():
    if not 'uid' in session:
        return render_template('alert3.html', msg='로그인이 필요한 서비스 입니다')
    resp = make_response(render_template('main.html', config=config) )
    # 쿠키 세팅
    resp.set_cookie('uid', session['uid'])
    return resp