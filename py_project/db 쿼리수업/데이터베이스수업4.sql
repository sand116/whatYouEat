select sname,code,name,cur from employees as e
join tbl_trade as t
on e.pname=t.name;
-- A,B교집합
select sname,code,name,cur from employees as e
inner join tbl_trade as t
on e.pname=t.name;
-- A-B + A,B교집합, 즉 A
select sname,code,name,cur from employees as e
left join tbl_trade as t
on e.pname=t.name;

-- B-A + A,B교집합, 즉 A
select sname,code,name,cur from employees as e
right join tbl_trade as t
on e.pname=t.name;

-- 데이터 요약 함수들 
-- AVG(평균)
select avg(cur) as avg_cur from tbl_trade;
-- count( 개수)
select count(cur) as cnt_cur from tbl_trade;
-- min(최소)
select min(cur) as min_cur from tbl_trade;
-- max(최대)
select max(cur) as max_cur from tbl_trade;
-- sum(총합)
select sum(cur) as _cur from tbl_trade;

-- 그룹바이 
select pname, count(*) as cnt from employees
group by pname;

select pname, count(*) as cnt from employees
group by pname having count(*)>1;
