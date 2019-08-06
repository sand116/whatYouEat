from service.model.dbMgr import DBHelper
# DBHelper 객체를 생성하는 역할만 담당
dbHelper=None
def createDBhelper(app) :
    global dbHelper
    #global dbHelper 이 변수는 함수 밖에 있는 전역 변수임을 알려줌
    dbHelper=DBHelper(app)



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

    