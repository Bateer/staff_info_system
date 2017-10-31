# ReadMe:
## 1. 项目名称: 员工工资管理系统
## 2. 作者: Ranger_Yu
## 3. 作业需求：
员工信息表程序，实现增删改查操作：
> 1. **可进行模糊查询，语法至少支持下面3种：**
  
>       select name,age from staff_table where age > 22
>     select * from staff_table where dept = "IT"
>     select * from staff_table where enroll_date like "2013

> **查到的信息，打印之后，最后面还要显示查到的条数**
> 2. **可创建新员工记录，以Phone做唯一键，staff_id自增**
> 3. **可删除指定员工信息记录，输入员工id，即可删除**
> 4. **可修改员工信息，语法如下：**

>       UPDATE staff_table SET dept="Market" where dept = "IT"
[详细描述参考 http://www.cnblogs.com/alex3714/articles/5740985.html2](http://www.cnblogs.com/alex3714/articles/5740985.html2)

## 4.实现效果：
直接运行文件main.py

----------Welcome----------
1. Inquire the information of staffs.

(You can use fuzzy sentence to inquire, For example: select name,age from staff_table.txt where age > 22.)
2. Create a new staff.
3. Delete staff.
4. Modification the information of staff.

(The syntax is: UPDATE staff_table.txt SET dept = Market WHERE where dept = IT)
5. Exit.

 Please your choice:
 
 **a.演示效果（模糊查询员工信息）**
 
 #### >>>1
 Please input: select name,age from staff_table.txt where age > 22

Syntax Right!

['Jack Wang', '30']

['Rain Liu', '25']

['Mack Cao', '40']

The number of information found is 3!

**b. 演示效果（以Phone为唯一键创建新的员工）**

 #### >>>2
 Please input your number: 183080465091
 
 The phone is able to be used!
 
 Please input your name:YU
 
 Age:25
 
 Dept:QA
 
 Enroll_date (Default format "1990-01-01"):2017-10-29
 
 [5, 'YU', '25', '18380465091', 'QA', '2017-10-29']
 
 **c. 演示效果（通过员工ID删除该员工信息）**
 #### >>>3
 Please input the id of the delete staff:5
 
 **d. 演示效果（修改信息中的员工信息）**
 #### >>>4
 Please input sentence about updating the information:
 
 UPDATE staff_table.txt SET dept = Market WHERE dept = IT
 Successfully modification!
 
 **e. 演示效果（退出）**
 #### >>>5
 Exit successfully!
 
## 5. 代码结构:
- 创建新员工函数(Function_Creation.py)
- 删除员工信息函数(Function_Delete.py)
- 查询员工信息函数(Function_inquire.py)
- 修改员工信息函数(Function_modification.py)
- 主函数(Main.py)
    - 用户交互界面（可供用户选择）
    - 调用对应的函数，并显示结果
    - 退出

## 6. 测试过程：

**a. 测试环境：**
    
    PyCharm Community Edition 2017.1.12 x64
    Python 3.6.1
    WINDOWS 10

**b. 测试所用员工名字和信息**

    1, Alex Li, 22, 13651054608, IT, 2013-04-01
    2, Jack Wang, 30, 13304320533, HR, 2015-05-03
    3, Rain Liu, 25, 1383235322, Sales, 2016-04-22
    4, Mack Cao, 40, 1356145343, HR, 2009-03-01
    5, YU, 25, 18380465091, QA, 2017-10-27

**c. 测试过程**

启动程序：

i. 用户输入选择：1 （用户模糊查询员工信息）
- 查询年龄大于22岁的员工的名字和年龄,查看打印结果：
> select name,age from staff_table.txt where age > 22
- 查询部门为‘IT’的员工的全部信息,查看打印结果：
> select  * from staff_table.txt where dept = IT
- 查询日期中含有‘2013’的员工全部信息,查看打印结果：
> select  * from staff_table.txt where enroll_date like 2013
- 任意模糊输入查询员工信息：
> select name,phone from staff_table.txt where phone like 13
- 语法输入错误，比如：
> select * from staff enroll_date 查看打印结果

ii. 用户输入选择：2 （创建新员工，以phone作为唯一键）

- 输入已经存在的电话号码，查看打印结果
- 输入一个错误格式的电话号码，查看打印结果
- 输入正确且在存贮文件不存在的电话号码，依次输入名字，年龄，电话号码，部门，入职时间，查看staff_table.txt中是否存储,员工id是否自增
> "5, YU, 25, 18380465091, QA, 2017-10-27"

iii. 用户输入选择：3 （删除员工信息）
- 输入需要删除的员工id（5），查看打印结果和存储文件中的变化
- 输入不存在的员工id，查看打印结果
- 输入员工的id不是数字，查看打印的结果

iiii. 用户输入选择：4 （更新员工信息）
- 输入正确的语法更新员工信息，查看存储文件staff_table.txt该员工信息的变化还有打印结果
> UPDATE staff_table.txt SET dept = Market WHERE dept = IT
- 输入错误的语法，查看显示结果
> Update staff_table.txt set dept = Market where dept = IT

iiiii. 用户输入选择：5 （退出）
- 查看显示结果以及程序是否退出

## 7. 小结
A. 在编写员工信息查询系统过程中，主要是遇到如何解析模糊查询，转化为三部分对文件中的信息进行操作以及筛选出来合适的信息，之后利用字典以及对应的序列还有列表分类解析出来。

B. 通过此次的编写，更够很好的理解利用函数来编程可以带来很多方便以及清晰的结构化。

C. 在程序中还存在很多不合理以及没有考虑全面的方面，在后面希望能够逐渐完善。