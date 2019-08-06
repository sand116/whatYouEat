-- 검색 쿼리
-- 연습 : tbl_epl 테이블의 모든 데이터를 가져오시오

select * form tbl_epl;
-- 순위 정보와 이름만 가져오기
-- as 컬럼 별칭 혹은 테이블 별칭

select rank as r, name from tbl_epl;

-- 순위를 역순으로, tbl_epl 테이블의 모든 데이터를 가져오시오
-- order by 기준 컬럼 desc(or asc)
select * from tbl_epl order by rank desc;
-- name 컬럼 값중에 '스'라는 텍스트가 들어가 row 데이터를 획득하시오.

select name from tbl_epl where name like '%스%';
select name from tbl_epl where name like '%맨체%';