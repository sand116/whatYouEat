data=[('프랑스','파리'),('이탈리아','로마'),('스페인','바로셀로나')]
for city2 in data:
    print(city2[0],city2[1])
print("-"*100)
data=[{'국가' :'프랑스','수도' :'파리'},{'국가':'이탈리아','수도':'마드리드'}]
for city3 in data:
    print(city3['국가'],city3['수도'])

#페이지 요청시 ->데이터 전달하기
###############################
#get
#http:127.0.0.1:5000/test?uid=k&upw=1
#서버에서 데이터 획득 방법
user_id=request.args.get('uid')
user_pw=request.args.get('upw')
################################
#post
#http:127.0.0.1:5000/test
#데이터는 http의 body를 타고 전달되어서 직접적으로 보이지 않는다
#서버에서 데이터 획득 방법
user_id=request.form['uid']
user_id=request.form['upw']