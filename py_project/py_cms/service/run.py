from flask import Flask,render_template,redirect,url_for,session, request, jsonify
from service.config import WebConfig
from service.model.dbMgr import loginSql,searchSql,selectAllEplList

#환경설정 클래스 모듈 가져오기
app = Flask(__name__)

#세션 생성에 필요한 세션키(중복되지않는 해쉬값 이용)를 정의
app.secret_key='iloveyou'
config=WebConfig() #config 생성
#세션이 없어도 접근 가능한 페이지는 오직 로그인


#세션 생성, 세션 종료, 세션 체크 
@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='GET':
        return render_template('login.html',config=config)
    else :
        uid=request.form['uid'] #post 방식으로 요청
        upw=request.form['upw']
        row=loginSql(uid=uid,upw=upw) #디비쿼리수행
        # false :[],(),{},0,""
        # row ->dit =>{..}
        # row에 uid upw name 저장
        if row :
            #세션처리(필요한 정보를 세션으로 저장한다) -서버 메모리에 저장
            session['uid']=uid
            session['name']=row['name']

            #세션종료
            return redirect(url_for('home'))
        else :
            return render_template('common/alert.2.html',msg='회원이 아닙니다')
    #경고창 ->되돌아가기


@app.route('/')
def home() :
    #세션이 없으면 /login으로 리다이렉트 
    # 만약 이 서버에 접속하는 사람이 2명이상일때도 이 조건문이 성립하는가?
    if not 'uid' in session :
        return redirect(url_for('login'))
    return render_template('index.html',config=config)

#로그아웃
@app.route('/logout')
def logout():
    if not 'uid' in session :
        return redirect(url_for('login'))
    #세션 종료
    print(session)
    if 'uid' in session:
        session.pop('uid',None)
    if 'name' in session:
        session.pop('name',None)
        print("*"*50)
    print('세션제거후 :',session)
    #페이지 요청을 리다이렉트 ->홈페이지
    return redirect(url_for('home'))

#eplList
@app.route('/eplList')
def eplList():
    rows=selectAllEplList();
    #세션 체크
    # if not 'uid' in session :
    #     return redirect(url_for('login'))
    #데이터 획득'
    #화면 처리
    amt = 5 #한번에 보여줄 양
    tmp = request.args.get("page") #전달된 페이지값 획득
    page  =0 #최종 페이지값 초기값
    if tmp : #전달된 페이지가 있다면 ex)eplList?page=2,...
        #페이지 계산 2로 전달되면 1로 계산해야함(쿼리기준)
        page=int(tmp)-1;
    #최종 결과 획득
    rows=selectAllEplList(page=page*amt)
    #화면 처리
    return render_template('eplList.html',config=config,epls=rows)


#검색 결과
@app.route("/search",methods=['POST'])
def search():
    keyword=request.form['m']

    tmp=searchSql(keyword)j

    if tmp == None : tmp=[]
    print(jsonify(tmp))
    return  jsonify(tmp)


if __name__ =="__main__" :
    app.run(debug=config.debug)

