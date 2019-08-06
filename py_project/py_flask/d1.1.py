'''
파이썬에서 mariadb를 접속하고, 쿼리 수행
1. 접속, 해제
2. 쿼리 수행:쿼리(QUERY)는 데이터베이스를 조작하는 언어
conn.cursor() 는 pymysql 에서 퀴리 수행을 위해서 사용하는 객체
#쿼리를 알지 못하니깐 툴에서 해결
'''
import pymysql as my
try:
    #  db 오픈
    conn=my.connect( host='127.0.0.1',
                #port=''database의 ip주소 3306번인 경우 기본값이니깐 안 바꿔도 됨
                user='root',
                password='811201',
                db='pythondb',
                charset='utf8',
                cursorclass=pymysql.cursors.DictCursor)
    print("연결 성공")
    #####################################################################
    #쿼리 수행 절차

    # 1. 커서 획득
    cursor=conn.cursor() #pythondb를 가리키는 것..?

    # 2. sql 준비 -쿼리
    sql= '''
    select
	    *
    from
	    tbl_users
    where
	    uid='1' and upw='1';
    '''
    # 3. 쿼리 수행
    cursor.execute(sql) #python db를 이용한 sql을 준비

    # 4. select한 결과 집합이 리턴됨 -> 결과 패치
    rows = cursor.fetchall()
    # print(rows)
    # for row in rows :
    #     print(rows[3])

    ########################################################################
    # 디비 닫기
    conn.close()
    print("닫기 성공")
except Exception as e: #죽지 않게 !
    print(e)