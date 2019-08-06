from service.model.dbMgr import DBHelper
dbHelper = None

# DBHelper 객체를 생성하는 역할만 담당
def createDBHelper( app ):
    # global dbHelper 이 변수는 함수 밖에 있는 전역 변수임을 알려줌
    global dbHelper
    dbHelper = DBHelper( app )

# 게시물 한개들 담는 그릇(최소로 필요한 것만 정의했음)
class PostModel:
    title   = None
    content = None
    writer  = None
    file    = None
    def __init__(self, title, content, writer, file):
        self.title   = title
        self.content = content
        self.writer  = writer
        self.file    = file