mysql练习

# 找最大

## fail

```sql
SELECT *FROM orders
WHERE order_date=MAX(order_date)
错误代码： 1111
Invalid use of group function
在where子句中order_date就已经是一条记录中的某个值了，取不了最大
只能用子查询找到最大
```



## sus

```sql
SELECT *FROM orders
WHERE order_date=
(
	SELECT MAX(order_date)FROM orders
)
```



# 找倒数第三大

## sus

```sql
select *from employees
order by hire_date desc
limit 2,1
```



# 对比inner 和left



请你查找所有已经分配部门的员工的last_name和first_name以及dept_no，未分配的部门的员工不显示

因为是inner join所以只有二者的emp_no都存在的时候才会显示

```sql
select e.last_name,e.first_name,d.dept_no
from dept_emp as d inner join employees as e
on d.emp_no=e.emp_no
```

请你查找所有已经分配部门的员工的last_name和first_name以及dept_no，也包括暂时没有分配具体部门的员工

因为是left join，所以employees表的所有内容都会被显示，如果没有找到dept_no字段，会显示null

```sql
select e.last_name,e.first_name,d.dept_no
from employees as e left join dept_emp as d
on e.emp_no=d.emp_no
```

# 