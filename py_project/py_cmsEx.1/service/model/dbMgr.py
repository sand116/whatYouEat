
'''
pip install DBUtils
DBUtils 의 풀링 기술을 이용하여 전체적으로 쿼리 처리 업그레이드
'''
import pymysql as my
from DBUtils.PooledDB import PooledDB
#from service.model import PostModel



#게시물 한개를 담는 그릇
class PostModel :
    title=None
    content=None
    writer=None
    file=None
    def __init__(self,title,content,writer, file):
        self.title=title
        self.content=content
        self.writer=writer
        self.file=file


DB_URL         =    'localhost' #127.0.0.1와 같음
DB_PORT        =    3306
DB_USER        =    'root'
DB_PASSWORD    =    '811201'
DB_DATABASE    =    'pythondb'
DB_CHARSET     =    'utf8'
MAX_POOL       =    100 #동접 백명 커버 가능 -보통 250명...

class DBHelper :
    #멤버 변수
    app=None
    #풀링 객체(디비와 연결된 커넥션을 가지고 있는 객체)
    connectionPool=None
    #생성자
    def __init__(self, application=None):
        self.app=application
        if self.app: #flask 객체가 존재하면 환경번수에서 뽑아서 세팅, 없으면 전역변수 값 사용
            DB_URL         =    self.app.config['DB_URL'] #127.0.0.1와 같음
            DB_PORT        =    self.app.config['DB_USER']
            DB_USER        =    self.app.config['DB_USER']
            DB_PASSWORD    =    self.app.config['DB_PASSWORD']
            DB_DATABASE    =    self.app.config['DB_DATABASE']
            DB_CHARSET     =    self.app.config['DB_CHARSET']
            MAX_POOL       =    self.app.config['MAX_POOL']

        self.initPool()
    #소멸자
    #del 객체명
    def __del__(self) :
        self.freePool()

    #멤버 함수
    #커넥션 풀을 생성
    def initPool(self) :
        self.connectionPool=PooledDB(creator=my,
                                host=DB_URL,
                                user=DB_USER,
                                password=DB_PASSWORD,
                                database=DB_DATABASE,
                                autocommit=False,#updata,delete,insert 한 후 반영하는 것
                                charset=DB_CHARSET,
                                cursorclass=my.cursors.DictCursor,
                                blocking=False,
                                maxconnections=MAX_POOL)
    #커넥션 풀해제
    def freePool(self) :
        #디비와 연결된 모든 커넥션을 닫는다.
        self.connectionPool.close()
    
    #개별 쿼리
    #로그인 처리

    #함수의 인풋 받았음 - 로그인 처리
    def loginSql(self,uid,upw) :
        rows =None       
        try:
            #커넥션을 풀링객체에서 빌려온다
            conn= self.connectionPool.connection()
            #쿼리 수행============================= 
            cursor=conn.cursor() 
            sql= '''
            select
                *
            from
                tbl_users
            where
                uid=%s and upw=%s;
            '''
            cursor.execute(sql,(uid,upw)) 
            rows = cursor.fetchone()
            cursor.close()
            #=====================================
            conn.close() #풀링에 반납한다.     
        except Exception as e: 
            print(e)
            rows=None
        finally :
            return rows

    #검색 처리
    def searchSql(self,keyword) :
        rows =None       
        try:
            #  db 오픈
            conn= self.connectionPool.connection()
            #####################################################################
            #쿼리 수행 절차
            # 쿼리
            cursor=conn.cursor() 
            sql= "select name,rank from tbl_epl where name like '%{0}%';".format(keyword)
            cursor.execute(sql) 
            rows = cursor.fetchall()
            cursor.close()
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
    def selectTeamName(self,teamName) :
        rows =None       
        try:
            conn= self.connectionPool.connection()
            cursor=conn.cursor()
            sql = '''
                select
                    *
                from
                    tbl_epl
                where
                    name = %s;              
                '''                  ## 약식표현으로 하면 겹침 

            # 3. 쿼리 수행
            cursor.execute( sql, (teamName) ) ## teamName이 튜플
            rows = cursor.fetchone()  
            cursor.close()
            conn.close()
            
        except Exception as e: #죽지 않게 !
            rows=None
        return rows
        
    #팀정보 수정(총경기수만 수정)
    def updateTeamInfo(self,total,teamName):
        results=None    
        try:
            conn= self.connectionPool.connection()
            #####################################################################
            #쿼리 수행 절차
            # 쿼리
            cursor=conn.cursor()  #pythondb를 가리키는 것..?
            sql= "update tbl_epl set total=%s where name=%s;"
            cursor.execute(sql,(total,teamName))
            #커밋(디비에 실제 반영)
            cursor.close()
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
    def selectAllEplList(self, stdCol='rank', order='asc', page=0, amt=5) :
    # 기본값은 혹시나 none이 들어갈까봐 미리해야함.    
        rows=None    
        try:
            conn= self.connectionPool.connection()
            cursor=conn.cursor() 
            sql= '''select rank, name, winPoint, win from tbl_epl
            order by %s %s 
            limit %s,%s;'''%(stdCol,order,page,amt)
            cursor.execute( sql )
            rows=cursor.fetchall()
            cursor.close()
            #fetchall이면 [{한 행}.{한 행},{한 행}]맨 앞에 해당하는 행만 추출하고 싶다면 fetchone()
            conn.close()

        except Exception as e: 
            rows=None
        return rows

    #게시물 모두 가져오기
    def selectAllBbs(self) : pass

    #게시물 등록
    def insertPost(self,pm) : 
        results=None    
        try:
            conn= self.connectionPool.connection()
            #####################################################################
            #쿼리 수행 절차
            # 쿼리
            cursor=conn.cursor()  #pythondb를 가리키는 것..?
            sql= '''insert into tbl_bbs
            (title,content,`file`,writter,regdate)
            values
            (%s,%s,%s,%s,now());
            '''
            cursor.execute(sql,(pm.title,pm.content,pm.file,pm.writer))
            #커밋(디비에 실제 반영)
            cursor.close()
            conn.commit()
            #results=conn.affected_rows()
                
                # print(rows) #[ {같은 행에 속하는 코럼name:값,콜럼rank: 값},{},{},{}]
                #sql 수행시 db에 해당 정보가 없으면 none반환
                # fetchone() 1개만 가져온다 ->리스트 형태가 제외되어 딕셔너리 형태만 오게됨
            ########################################################################
            # 디비 닫기
            conn.close()
            # print("닫기 성공")
            
        except Exception as e: #죽지 않게 !
            print(e)
            results=None
        return results

        
if __name__== '__main__' :
    #함수에 아이디 비번 넣어서 회원 여부 조회 결과를 받는다.
    # results=loginSql('2','2') #함수는 호출해야 작동
    # results=selectTeamName('번리 FC')
    # print(results)
    # print("결과 :",results)
    # rows=selectAllEplList()
    # print(rows)
    #pass
    obj=DBHelper() #클래스 객체 생성
    param=PostModel('제목1','내용1','작성자1','파일경로')
    print(obj.insertPost(param))
    #print(obj.loginSql('1','1'))