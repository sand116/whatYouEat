-- ======================================= --
-- 조회, 필터링, 검색, 정렬, 조인, 요약 등
-- select
-- ======================================= --
-- 데이터베이서에서 데이터를 가져오는 명령 select
-- 모든 데이터 조회
select * from tbl_trade;

-- 특정 컬럼만 조회
select code, name, cur from tbl_trade;

-- 필터링 : where 
-- alter table tbl_trade 
-- modify cur int;
-- 현재가가 1000000이상인 주식만 출력하시오
select * from tbl_trade where cur > 1000000;

-- 논리연산 AND or 혼합 (우선순위 AND > or)
-- updown 컬럼을 float 형으로 변경하시오
alter table tbl_trade modify updown float;
-- 현재가가 1000000 이고, 등락폭 0 이상인 주식만
select * from tbl_trade where cur>100000 and updown>0;

select * from tbl_trade where cur>100000 or updown>0;

-- in (여러개를 열거하는 경우)
select * from tbl_trade
where name='SK하이닉스' or name='현대차';

select * from tbl_trade 
where name in ('SK하이닉스', '현대차');

-- 검색 (일부 정보만을 가지교 데이터를 찾을때)
select * from tbl_trade 
where name like '삼%';

-- 정렬
select * from tbl_trade 
where name like '삼%' order by name desc;

-- 조인 (두개 이상 테이블의 특정 컬럼을 연결하여)
-- 새로운 데이터를 획득
-- 조인, inner join, outter join, left(right) join,
-- self join 





