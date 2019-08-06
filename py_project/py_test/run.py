#pip install selenium
from selenium import webdriver as wd
import time

# 기본 접속 사이트
MAIN_URL='https://news.naver.com/main/ranking/read.nhn?m_view=1&mid=etc&sid1=111&rankingType=popular_day&oid=001&aid=0010217256&date=20180718&type=1&rankingSeq=1&rankingSectionId=100'

# 브라우저 따오기
driver= wd.Chrome(executable_path='./chromedriver.exe')
# 접속
driver.get(MAIN_URL)
# 캡쳐 (고스트에서 주로 진행을 함 - 팬텀js)
driver.save_screenshot('main.png')
# 검색 (검색창의 아이디는 : SearchGNBText)
# 사이트 페이지가 로드되는 것(브라우저 메모리에 로드되는 시점)
# 2초 대기후 진행
driver.implicitly_wait(2)
driver.find_element_by_id('u_cbox_guide').send_keys('예뻐요') #input 태그 찾음

# #검색 클릭
# driver.find_element_by_class_name("u_cbox_guide").click()