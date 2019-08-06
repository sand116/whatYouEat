from flask import Flask, render_template, redirect, url_for, session, request, jsonify, make_response
from service.controller import bp_my as app
# 디비
from service.model import dbHelper
from service import config

@app.route('/page', methods=['GET','POST'])
def mypage():
    if request.method == 'POST':
        result = request.form

        weight=request.form['weight']
        height=request.form['height']
        age=request.form['age']
        gender=request.form['gender']

        if gender=='F':
            basic = 655.1 + (9.56 * float(weight)) + (1.85 * float(height)) - (4.68 * float(age))
        else:
            basic =  66.47 + (13.75 * float(weight)) + (5 * float(height)) - (6.76 * float(age))  
        result.basic=round(float(basic),2)
        
        # result.data= db에서 가져온 데이타
        # print(result)
        return render_template('mypage.html',result=result)
    
    else:
        result = request.args
        return render_template('mypage.html',result=result)


@app.route('/page_edit', methods=['GET','POST'])
def mypageEdit():
    if request.method == 'POST':
        return render_template('mypage_edit.html')
    else:
        return render_template('mypage.html')


@app.route('/dash_board', methods=['get'])
def chart(code):
    row = dbHelper.chart(code)
    print(row)
    return render_template('dash_board.html', row=row)