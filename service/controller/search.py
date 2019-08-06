from flask import Flask, render_template, redirect, url_for, session, request, jsonify, make_response
from service.controller import bp_search as app
# 디비
from service.model import dbHelper
from service import config

@app.route('/search', methods=['POST'])
# home 검색창에서 음식을 검색하면 
# 아래 search 서버에서 search.html을 띄워 검색결과를 보여준다 
def search():
    # keyword = request.form['keyword']
    # tmp     = dbHelper.searchSql(keyword)
    # if tmp == None: tmp=[]
    # return jsonify(tmp)
    # print(tmp)
    fname = request.form['fname']
    rows = dbHelper.searchSql(fname)
    return render_template('search.html', rows=rows)

# @app.route('/food', methods=['get'])
# # 사진을 누르면 상품 상세 페이지를 뜨게한다 
# def food():
    
#     tmp = request.args.get('code')
#     return render_template('sub/food_sub.html')
#     #get방식으로 사진 여러개 각각마다 사진 정보를 띄움.

@app.route('/food/<code>', methods=['get'])
# 사진을 누르면 상품 상세 페이지를 뜨게한다 
def food_code(code):
    # code = request.args.get('code')
    
    row = dbHelper.food_info(code)
    print(row)
    return render_template('sub/food_sub.html', row=row)

# @app.route('/chart/<id>', methods=['get'])
# def chart(code):
#     row = dbHelper.chart(code)
#     print(row)
#     return render_template('sub/food_sub.html', row=row)

@app.route('/eat', methods=['POST'])
def eat():
    code = request.form['code']
    row = dbHelper.food_info(code)
    return render_template('sub/food_sub1.html',code=code, row=row)


@app.route('/detail', methods=['get'])
# 사진을 누르면 상품 상세 페이지를 뜨게한다 
def detail(): pass
    #get방식으로 사진 여러개 각각마다 사진 정보를 띄움.


############################################################################
#스낵
@app.route('/snack', methods=['get'])
# 사진을 누르면 상품 상세 페이지를 뜨게한다 
def snack(): pass
    #get방식으로 사진 여러개 각각마다 사진 정보를 띄움.

#라면
@app.route('/ramen', methods=['get'])
# 사진을 누르면 상품 상세 페이지를 뜨게한다 
def ramen(): pass
    #get방식으로 사진 여러개 각각마다 사진 정보를 띄움.

#아이스크림
@app.route('/icecream', methods=['get'])
# 사진을 누르면 상품 상세 페이지를 뜨게한다 
def icecream(): pass
    #get방식으로 사진 여러개 각각마다 사진 정보를 띄움.
    