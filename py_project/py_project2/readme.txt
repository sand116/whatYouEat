데이터분석, 통계
- db 설계
- 화면,기능 설계
- er 다이어그램
- 데이터 분석
  1.  데이터 수집(엑셀 , csv 파일을 다운받거나
       크롤링-   beautifulsoup, selenium)
  2.  데이터 전처리(preprocessing) - 업무의 90%
  3.  데이터 분석,통계
  4.  시각화  


sungback@naver.com
평생 a/s
 [회원 테이블]
 아이디 (primary키 =pk) <논리적인 설계- 머릿속에서 설계>
 이름
 나이
 주소
 전화번호
 성별

 물리적인 설계-실제구현을 위한 준비 단계

[member]
id  VARCHAR(20) NOT NULL
name  VARCHAR(20) NOT NULL
age int NOT NULL
address VARCHAR(100)  NOT NULL
phone VARCHAR(13) NOT NULL
gender  VARCHAR(1)  NOT NULL

반드시 입력해야하는 값은 NOT NULL설정

시각화 : matplotlib
        seaborn