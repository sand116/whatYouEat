-- 마리아 db 접속
-- mysql [-u 사용자명][-p]-패스워드 [-h host] [데이터베이스 명
mysql -u root -p
Enter password: ****
-- 접속 후 프럼프트
-- 마리아 데이터베이스에 접속했다, [디비명표시]
MariaDB[(none)]

-- 사용하고자 하는 디비 지정
use pythondb;
MariaDB[(pythondb)]
-- 데이터 베이스의 목적->데이터를 저장한다
-- 구조 :row + column 2차원 구
-- row=하나의 레코드, 레코드는 여러개의 컬럼을 가질 수 있다.
-- 하나의 데이터베이스에는 여러개의 테이블이 존재할 수 있다.
-- 여러 테이블들의 컬럼들이 서로 관계를 맺을 수 있다. (데이터의 연결)
-- => 관계형 데이터 베이스 RDBMS <-> No sql 계열 몽고 디비,..-> 클라우드, 빅데이터(계속 수집되는 경향),...
-- 마리아 디비 족보
-- my sql이 오픈 소스 기반 사용 -> sun(java 만든 곳) 인수 -> 오라클 인수 -> 상업적으로 가게됨
-- ->개발자 떨어져 나감 -> 오픈 기반에 맞춰 마리아디비 만들어짐 -> 구글 지원
--  mysql의 엔터프라이즈 기반 -> aws에서 오로라 디비 발전


-- 서버에 있는 모든 데이터 베이스 보기
show databases;

-- 데이터 베이스 생성
create database <데이터베이스명>
-- 데이터베이스가 없으면 만들어라 
create database if not exists my_db;

-- sql은 데이터 베이스와 개발자가 상호 소통하는 언어이다
-- db와 소통할수 있는 언어를 배우는 과정 
-- 데이터 베이스 삭제
drop database if exists my_db;

-- ======================================= --
-- 테이블 생성, 변경, 삭제 등
-- --------------------------------------- --
create table 테이블명( <컬럼정의>,...);

-- 컬럼 구조
<컬럼명> <데이터 타입>
[ NOT NULL | NULL]
[ default <기본값>]
[ AUTO_INCREMENT]
[ UNIQUE [KEY] | PRIMARY KEY]
[ COMMENT '<주석>']

create table employees (
 id int not null auto_increment primary key, -- auto increment 자동증가 
 sname varchar(100),
 gname varchar(100),
 pname varchar(50),
 birthday date comment '생년월일'
 );
 -- 생성된 테이블의 생성쿼리 확인
 show create table employees;
-- ENGINE=InnoDB DEFAULT CHARSET=utf8 이부분은 마리아디비가 자동으로 추가한 부분 
-- 테이블의 구조 보기
describe employees;

-- 테이블 변경
alter table 테이블이름 <변경 내용 기술> [,변경내용정의]..pythondb

-- 컬럼 추가(first, after pname, 생략)
alter table employees
add username varchar(20)
after pname;
describe employees;
-- 컬럼 변경
alter table employees 
modify username varchar(30);

-- 컬럼 삭제
alter table employees 
drop username;


-- 테이블 삭제
-- drop table employees;
drop table if exists employees;

-- ====================================================== --
-- 입력(insert), 수정(update), 삭제(delete)
-- ======================================================= --

-- 입력 
insert into <테이블명 - 대괄호 생략 가능 > [<컬러명>,...] 
{values | value} ({<표현식>|default},...)
-- 컬럼 없이 입력 => 전체 입력을 하겠다 -> 순서주의

insert into employees
values (NULL,'GOOD','MILLER','KIM','2018-01-01' );

-- 특정 컬럼만 입력 -> 이경우 순서 변경가능
insert into employees (gname,sname) 
values ('GOOD2','MILLER2');

-- 한번에 왕창 넣기
insert into employees values
(NULL,'GOOD3','MILLER3',NULL,NULL ),
(NULL,'GOOD4','MILLER4',NULL,NULL ),
(NULL,'GOOD5','MILLER5',NULL,NULL );

-- 다른 테이블에 데이터를 넣기
insert into employees (sname)
select name from tbl_users;
-- 파일에서 로드해서 데이터 넣기
load data infile "C:/Users/박진경/Desktop/data.txt"
into table employees (sname, gname, pname);

-- 기존 데이터 변경 
update <테이블명>
set 컬러명-{표현식| default},/..,,,
where <조건>

-- 특정 조건에 맞는 레코드로의 특정 컬럼을 수정
update employees set pname='LEE'
where pname='Kim';

-- 특정 컬럼의 데이터 중 특정 문자를 대체 처리, 제거
update tbl_trade set cur=replace(cur,',','');
-- where문이 없으므로 싹다

-- 삭제 
delete from <테이블명< [where 조건]

delete from employees where sname='멀티2';

