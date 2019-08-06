-- 직원들이 가지고 잇는 주식을 정보중(이름, 
-- 종목코드, 현재가) 정보와  직원의 이름을 같이 
-- 연결하여 출력하시오
select sname, code, name, cur from employees as e
join tbl_trade as t
on e.pname = t.name;

select sname, code, name, cur from employees as e
inner join tbl_trade as t
on e.pname = t.name;

select sname, code, name, cur from employees as e
left join tbl_trade as t
on e.pname = t.name;

select sname, code, name, cur from employees as e
right join tbl_trade as t
on e.pname = t.name;