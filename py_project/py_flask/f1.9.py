
from flask import Flask,request,render_template

app = Flask(__name__)

#  @ : 데코레이터
@app.route('/')
def home() : 
    #teams 안에 팀을 하나씩 출력하시오
    teams=[{'rank':1,'team' :'프랑스'},
    {'rank':2,'team':'벨기에'},
    {'rank':3,'team':'잉글랜드'},
    {'rank':4,'team':'크로아티아'}]
    a=1
    for team in teams :
        #랭킹하고 팀명 출력
        print(team['rank'],team['team'])
    
    return render_template("index.html",title='제목',teams=teams,i=i)

if __name__ =="__main__" :
    app.run(debug=True)