--Первый пункт: создание таблицы
create table employees (
name varchar(50),
position int,
department varchar(50),
salary decimal(10,2)
);

--Второй пункт: добавление данных
insert into employees (name, position, department, salary)
values ('John Doe', 1, 'manager', 40000.00),
('Bryce Waine', 2, 'sales', 70000.00),
('Jacki Chan', 3, 'manager', 30000.00),
('Will Smith', 4, 'IT', 60000.00);

--Третий пункт: измкнение данных о сотруднике
update employees set salary = 70000.00 where name = 'Jacki Chan';

--Четвертый пункт и пятый пункт: добавление нового столбца с добавлением записи для всех сотрудников
alter table employees 
add column hiredate date default '2001-05-15';

--Шестой пункт: Поиск сотрудников 'manager'
select name from employees where department = 'manager';

--Cедьмой пункт: Поиск сотрудников у которых >50000.00
select name from employees where salary > 50000.00;

--Восьмой пукт: Поиск сотрудников 'sales'
select name from employees where department = 'sales';

--Девятый пункт: Вывод средней ЗП у всех сотрудников
create function get_avg_salary()
returns numeric 
as $$
declare
avg_salary numeric;
begin
	select avg(salary) into avg_salary from employees;
	return avg_salary;
end;
$$ language plpgsql;

select get_avg_salary();

--Десятый пункт: Удаление таблицы
delete table employees 