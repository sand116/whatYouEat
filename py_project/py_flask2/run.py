from flask import Flask, request, url_for, render_template,redirect,jsonify
from model.d1_8 import searchSql,selectTeamName,updateTeamInfo
#flask 클래스를 이용하여 서버를 만듬
app=Flask(__name__)
#페이지구성

#홈페이지 ~/
@app.route("/")
def home() :
    return render_template('index.html',title='홈페이지')
#index.html 을 기본 홈으로 봄

@app.route("/join")
def join():
    return render_template('test.1.html',title='회원가입')


@app.route("/search",methods=['POST']) #html에서 post 방식 json형태로 사용자에게 입력된 keyword 보내기
def search():
    keyword=request.form['m']
    #디비로 검색어를 보내서 쿼리 수행후 결과를 받아준다.
    #디비 폴더를 따로 만든 것은 이를 패키지로 사용하겠다는 의미..!! __init__파일생성해야함

    tmp=searchSql(keyword)
    # None 이면 json 변환에 문제가 발생하므로 비워있는 리스트로 대체
    if tmp == None : tmp=[]
    print(jsonify(tmp))
    return  jsonify(tmp)
    #jsonfy() : 파이썬 객체를 json 문자열로 처리-> 전송


#팀 세부 정보 보기
@app.route('/info/<teamName>')
def info(teamName) :
    q=request.args.get('q')
    print('q=%s'%q)
    row=selectTeamName(teamName)
    #q값이 none이면 그냥 정보보기, uptate이면 수정히기이다.
    return render_template('info.html',team=row,flag=q)

#팀 정보 수정 페이지

@app.route('/updateTeam',methods=['POST'])
def updateTeam() :
    #전달된 데이터 중 경기수와 이름을 획득
    total=request.form['total']
    name=request.form['name']
    #수정 쿼리를 수행
    result=updateTeamInfo(total,name)
    #결과 처리
    if result :
        return render_template("alert.2.html",msg='수정성공',url='/info/'+name)
    else :
        return render_template("alert.2.html",msg='수정실패')

if __name__=='__main__' :
    app.run(debug=True)

#자바 스크립트에서 제공하는 프레임워크  중 무료로 제공되는 것이  startbootstrap - 부트스트랩 - sb adim v20
#static 폴더를 넣으면 라우팅을 하지 않아도(주소 입력하지 않아도),, 알아서 인식 가능 