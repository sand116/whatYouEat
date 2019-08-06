#셀레니움은 어디 사이트를 가서 내가 하고싶은 행동을 하는 부분 ex)드루킹

#뷰리폴수프는 어디 사이트에 내가 원하는 정보를 뽑아낼때 사용
from urllib.request import urlopen #웹사이트 url 열어주는 역할
from bs4 import BeautifulSoup
html=urlopen("http://www.nlotto.co.kr/gameResult.do?method=byWin")
soup=BeautifulSoup(html,'html.parser')
#print(soup.prettify())
hoi=soup.find("h3", {'class' : 'result_title'}) 
print(hoi.strong.string, '회')
p=soup.find('p',{'class':'number'})#p태그 클래스 : number
imgs=p.find_all('img') #.find로 계속 안에 있는 것(태그) 찾아내기 -리스트에 담아 모든 것을출력
# numbers=[]
# for i in imgs : #한 태그의 속성 접근
#     numbers.append(i['alt'])
# print(numbers)
# #이미지 태그 담기
numbers=[ img['alt'] for img in imgs ] #리스트 안에 넣기
print(numbers)
bonus=numbers.pop() # 맨 뒤에 연걸
print(bonus)