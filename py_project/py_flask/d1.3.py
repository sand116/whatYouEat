'''
파이썬에서 mariadb를 접속하고, 쿼리 수행
1. 접속, 해제
2. 쿼리 수행:쿼리(QUERY)는 데이터베이스를 조작하는 언어
#쿼리를 알지 못하니깐 툴에서 해결
3. 기본 커서는 데이터를 오직 순서대로만 보내기 때문에 테이블 컬럼의 위치가 변경되거나,
쿼리문이 조정되면 순서가 바뀌게 되어서 소스를 수정해야 하는 상황이 벌어진다.
=>해결방안 =>컬ㄹ럼이 따라와서 딕셔너리 형태로 가면
=>순서가 의미 없으므로 자동으로 해결된다
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
    cursor.execute(sql)#python db에서 이 sql을 준비

    # 4. select -> 결과 집합이 리턴됨 -> 결과 패치
    rows = cursor.fetchall()
    print(rows)
    for row in rows:
        print(row['name'])

    ########################################################################
    # 디비 닫기
    conn.close()
    print("닫기 성공")
except Exception as e: #죽지 않게 !
    print(e)