'''
파이썬에서 mariadb를 접속하고, 쿼리 수행
1. 접속, 해제
2. 쿼리 수행:쿼리(QUERY)는 데이터베이스를 조작하는 언어
#쿼리를 알지 못하니깐 툴에서 해결

3. 기본 커서는 데이터를 오직 순서대로만 보내기 때문에 테이블 컬럼의 위치가 변경되거나,
쿼리문이 조정되면 순서가 바뀌게 되어서 소스를 수정해야 하는 상황이 벌어진다.
=>해결방안 =>컬럼이 따라와서 딕셔너리 형태로 가면
=>순서가 의미 없으므로 자동으로 해결된다
4. 쿼리문에 인자를 전달하여 수행하기 -일반화 기본 작업 
5. with문을 이용하여 커서 닫기를 자동으로 처리
6. 함수화를 통해서 누구나, 혹은 여러번 호출만으로 이 기능을 사용하게 처리
-->재사용성 높이기
7.  함수에 리턴값을 부여하여 퀴리 결과를 돌려주게 처리
8. 모듈화를 위한 처리
'''
import pymysql as my
#함수의 인풋 받았음
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
            rows = cursor.fetchall()
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


if __name__== '__main__' :
    #함수에 아이디 비번 넣어서 회원 여부 조회 결과를 받는다.
    results=loginSql('2','2') #함수는 호출해야 작동
    print(results)

