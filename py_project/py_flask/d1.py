'''
파이썬에서 mariadb를 접속하고, 쿼리 수행
1. 접속, 해제
'''
import pymysql as my
try:
    #  db 오픈
    conn=my.connect( host='127.0.0.1',
                #port=''database의 ip주소 3306번인 경우 기본값이니깐 안 바꿔도 됨
                user='root',
                password='811201',
                db='pythondb',
                charset='utf8')
    print("연결 성공")
    # 디비 닫기
    conn.close()
    print("닫기 성공")
except Exception as e: #죽지 않게 !
    print(e)