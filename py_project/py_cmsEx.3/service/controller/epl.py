from flask import Flask,render_template,redirect,url_for,session, request, jsonify, make_response
from service.controller import bp_epl as app
#디비
from service.model import dbHelper #객체 변수 땡겨옴
from service import config

#eplList
#~/epl/eplList
@app.route('/eplList')
def eplList():
#세션 체크
# if not 'uid' in session :
#     return redirect(url_for('login'))
#데이터 획득'
#화면 처리
#한번에 보여줄 양
    amt = 5 
    tmp = request.args.get("page") #전달된 페이지값 획득
    page =0 #최종 페이지값 초기값
    if tmp : #전달된 페이지가 있다면 ex)eplList?page=2,...
        #페이지 계산 2로 전달되면 1로 계산해야함(쿼리기준)
        page=int(tmp)-1;
    #최종 결과 획득
    rows=dbHelper.selectAllEplList(page=page*amt)
    #화면 처리
    return render_template('eplList.html',config=config,epls=rows)


#검색 결과
#~/epl/search
@app.route("/search",methods=['POST'])
def search():
    keyword=request.form['m']
    tmp=dbHelper.searchSql(keyword)

    if tmp == None : tmp=[]
    print(jsonify(tmp))
    return  jsonify(tmp)
