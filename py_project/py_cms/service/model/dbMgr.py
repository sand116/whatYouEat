
import pymysql as my
#from service.config import WebConfig
#함수의 인풋 받았음 - 로그인 처리
def loginSql(uid,upw) :
    rows =None       
    try:
        #  db 오픈
        conn=my.connect( host='127.0.0.1',
                    #port=''database의 ip주소 3306번인 경우 기본값이니깐 안 바꿔도 됨
                    user='root',
                    password='811201',
                    db='pythondb',
                    charset='utf8')
        #####################################################################
        #쿼리 수행 절차

        # 1. 커서 획득

        with conn.cursor(my.cursors.DictCursor) as cursor : #pythondb를 가리키는 것..?

            # 2. sql 준비 -쿼리
            sql= '''
            select
                *
            from
                tbl_users
            where
                uid=%s and upw=%s;
            '''
            # 3. 쿼리 수행
            cursor.execute(sql,(uid,upw)) #python db에서 이 sql을 준비
            #뒤에 튜플은 sql에 전달
    
            # 4. select에서의 결과 집합이 리턴됨 -> 결과 패치
            rows = cursor.fetchone()
            # print(rows)
            # for row in rows:
            #     print(row['name'])
            
            #5. 커서 닫기 -> 자동으로 됨
            #cursor.close()

        ########################################################################
        # 디비 닫기
        # conn.close()
        # print("닫기 성공")
        
    except Exception as e: #죽지 않게 !
        print(e)
    #else : 오류 없으면
    finally : #무조건 탐
        return rows


#검색 처리
def searchSql(keyword) :
    rows =None       
    try:
        #  db 오픈
        conn=my.connect( host='127.0.0.1',
                    #port=''database의 ip주소 3306번인 경우 기본값이니깐 안 바꿔도 됨
                    user='root',
                    password='811201',
                    db='pythondb',
                    charset='utf8',
                    cursorclass=my.cursors.DictCursor)
        #####################################################################
        #쿼리 수행 절차
        # 쿼리
        with conn.cursor(my.cursors.DictCursor) as cursor : #pythondb를 가리키는 것..?
            sql= "select name,rank from tbl_epl where name like '%{0}%';".format(keyword)
            cursor.execute(sql) 
            rows = cursor.fetchall()
            print(rows) #[ {같은 행에 속하는 튜플(name):값,튜플(rank) 값},{},{},{}]
            #sql 수행시 db에 해당 정보가 없으면 none반환
        ########################################################################
        # 디비 닫기
        conn.close()
        # print("닫기 성공")
        
    except Exception as e: #죽지 않게 !
        rows=None
    return rows

#팀 검색
def selectTeamName(teamName) :
    rows =None       
    try:
        #  db 오픈
        conn=my.connect( host='127.0.0.1',
                    #port=''database의 ip주소 3306번인 경우 기본값이니깐 안 바꿔도 됨
                    user='root',
                    password='811201',
                    db='pythondb',
                    charset='utf8',
                    cursorclass=my.cursors.DictCursor)
        #####################################################################
        #쿼리 수행 절차
        # 쿼리
        with conn.cursor(my.cursors.DictCursor) as cursor : #pythondb를 가리키는 것..?
            sql= "select * from tbl_epl where name=%s;"
            cursor.execute(sql,(teamName)) 
            rows = cursor.fetchone()
            # print(rows) #[ {같은 행에 속하는 코럼name:값,콜럼rank: 값},{},{},{}]
            #sql 수행시 db에 해당 정보가 없으면 none반환
            # fetchone() 1개만 가져온다 ->리스트 형태가 제외되어 딕셔너리 형태만 오게됨
        ########################################################################
        # 디비 닫기
        conn.close()
        # print("닫기 성공")
        
    except Exception as e: #죽지 않게 !
        rows=None
    return rows
    
#팀정보 수정(총경기수만 수정)
def updateTeamInfo(total,teamName):
    results=None    
    try:
        #  db 오픈
        conn=my.connect( host='127.0.0.1',
                    #port=''database의 ip주소 3306번인 경우 기본값이니깐 안 바꿔도 됨
                    user='root',
                    password='811201',
                    db='pythondb',
                    charset='utf8',
                    cursorclass=my.cursors.DictCursor)
        #####################################################################
        #쿼리 수행 절차
        # 쿼리
        with conn.cursor() as cursor : #pythondb를 가리키는 것..?
            sql= "update tbl_epl set total=%s where name=%s;"
            cursor.execute(sql,(total,teamName))
            #커밋(디비에 실제 반영)
            conn.commit()
            results=conn.affected_rows()
            # print(rows) #[ {같은 행에 속하는 코럼name:값,콜럼rank: 값},{},{},{}]
            #sql 수행시 db에 해당 정보가 없으면 none반환
            # fetchone() 1개만 가져온다 ->리스트 형태가 제외되어 딕셔너리 형태만 오게됨
        ########################################################################
        # 디비 닫기
            conn.close()
        # print("닫기 성공")
        
    except Exception as e: #죽지 않게 !
        results=None
    return results

#모든 팀 가져오기 (정렬기준 컬럼, 정렬방식, 시작페이지, 한페이지의 양  )
def selectAllEplList(stdCol='rank', order='asc', page=0, amt=5) :
# 기본값은 혹시나 none이 들어갈까봐 미리해야함.    
    rows=None    
    try:
        conn=my.connect( host='127.0.0.1',
                    user='root',
                    password='811201',
                    db='pythondb',
                    charset='utf8',
                    cursorclass=my.cursors.DictCursor)
        with conn.cursor() as cursor : 
            sql= '''select rank, name, winPoint, win from tbl_epl
             order by %s %s
            limit %s,%s;'''%(stdCol,order,page,amt)
            cursor.execute( sql )
            rows=cursor.fetchall() 
            #fetchall이면 [{한 행}.{한 행},{한 행}]맨 앞에 해당하는 행만 추출하고 싶다면 fetchone()
            conn.close()

    except Exception as e: 
        rows=None
    return rows
    
      
if __name__== '__main__' :
    #함수에 아이디 비번 넣어서 회원 여부 조회 결과를 받는다.
    # results=loginSql('2','2') #함수는 호출해야 작동
    # results=selectTeamName('번리 FC')
    # print(results)
   # print("결과 :",results)
    rows=selectAllEplList()
    print(rows)