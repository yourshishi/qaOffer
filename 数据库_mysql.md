#mysql

####参考： https://www.cnblogs.com/frankielf0921/p/5930743.html

###零、sql语句：
#####0.0 现在学生小测验成绩表table1（id，uid，name，score，stdate), 其属性分别表示自增id、学生学号、学生姓名、成绩和统计日期。查询每天成绩最高分，输出日期、最高分。
     select  stdate, max(score) from table1    group by stdate;

#####0.1用一条SQL语句：查询出每门课都大于80分的学生姓名
     select distinct name from table group by name having count(kecheng)>=3 and min(fenshu)>=80;
或者：
select name from (select name,min(score) from student group by name having min(score)>80) stu;

     select count(ordid) from odertable group by(uderid) bettewn ;

#####0.2 求工资第二高的人：
     select max(Salary) SecondHighestSalary from Employee where Salary <> (select max(Salary) from Employee );

#####0.3 建一个mysql表：
     CREATE TABLE `quicker_perf_plan` (
       `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '自身id',
       `jobname` varchar(255) DEFAULT NULL COMMENT '脚本名称',
       `createdata` datetime DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
        PRIMARY KEY (`id`)
     ) ENGINE=InnoDB AUTO_INCREMENT=4896 DEFAULT CHARSET=utf8mb4;


###一、数据库的事务：
事务（transaction）是作为一个单元的一组有序的数据库操作。如果组中的所有操作都成功，则认为事务成功，如果一个操作失败，则事务将回滚， 该事务所有操作的影响都将取消。
共享锁、排他锁；行级锁、表级锁；乐观锁、悲观锁；
四大隔离级别 （mcc锁实现） 

1.Read Committed（未提交读，可能引起脏读） 

2.Repeatable Read（已读提交） 

3.可重复读 

4.Serializable（可串行化）

###二、为什么说B+树比B树更适合数据库索引？
####2.1  B+树与B树最大的区别在于：
#####1、 B+叶子结点包含全部关键字以及指向相应记录的指针，而且叶结点中的关键字按大小顺序排列，相邻叶结点用指针连接
（B树的非叶子节点存储实际记录的指针，而B+树的叶子节点存储实际记录的指针，B+树的叶子节点通过指针连起来了, 适合扫描区间和顺序查找。）
#####2、B+非叶结点仅存储其子树的最大（或最小）关键字，可以看成是索引。
#####2.2  B+树更适合外部存储。由于内结点不存放真正的数据（只是存放其子树的最大或最小的关键字，作为索引），一个结点可以存储更多的关键字，每个结点能索引的范围更大更精确，也意味着B+树单次磁盘IO的信息量大于B树，I/O的次数相对减少。
#####2.3  MySQL是一种关系型数据库，区间访问是常见的一种情况，B+树叶结点增加的链指针，加强了区间访问性，可使用在区间查询的场景；而使用B树则无法进行区间查找。

###三、数据库索引：是数据库管理系统中一个排序的数据结构，以协助快速查询、更新数据库表中数据。索引的实现通常使用B树及其变种B+树。
b/b+树是为了存储而设计的一种平衡多路查找树，高度比二叉树小，能够降低磁盘的I/O次数： n个节点的平衡二叉树的高度为H(即logn)，而n个节点的B/B+树的高度为logt((n+1)/2)+1；

优点： 

第一，通过创建唯一性索引，可以保证数据库表中每一行数据的唯一性。

第二，可以大大加快数据的检索速度，这也是创建索引的最主要的原因。

第三，通过使用索引，可以在查询的过程中，使用优化隐藏器，提高系统的性能。

第四，可以加速表和表之间的连接，特别是在实现数据的参考完整性方面特别有意义。

第五，在使用分组和排序子句进行数据检索时，同样可以显著减少查询中分组和排序的时间。

缺点

第一，创建索引和维护索引要耗费时间，这种时间随着数据量的增加而增加。

第二，索引需要占物理空间。

第三，当对表中的数据进行增加、删除和修改的时候，索引也要动态的维护，这样就降低了数据的维护速度。

###四、mysql的三大引擎是啥？
mysql常用的引擎有InnoDB，MyISAM，Memory，默认是InnoDB，InnoDB：磁盘表，支持事务，支持行级锁，B+Tree索引

###五、你常用的mysql引擎有哪些？各引擎间有什么区别？ 
1）、InnoDB 支持事务，MyISAM 不支持

2）、MyISAM 适合查询以及插入为主的应用，InnoDB 适合频繁修改以及涉及到安全性较高的应用；

3）、MyISAM采用表级锁(table-level locking)。InnoDB支持行级锁(row-level locking)和表级锁,默认为行级锁。

4）、清空整个表时，InnoDB 是一行一行的删除，效率非常慢。MyISAM 则会重建表；

###六、CREATE INDEX 实例
本例会创建一个简单的索引，名为 "PersonIndex"，在 Person 表的 LastName 列：
CREATE INDEX PersonIndex   ON Person (LastName)

如果您希望以降序索引某个列中的值，您可以在列名称之后添加保留字 DESC：
CREATE INDEX PersonIndex   ON Person (LastName DESC) 

假如您希望索引不止一个列，您可以在括号中列出这些列的名称，用逗号隔开：
CREATE INDEX PersonIndex   ON Person (LastName, FirstName)


###七、mysql表比较大，查询慢，如何优化？

1.SQL语句优化（查看慢查询：有无监控报警；show processlist ；查看慢查询日志；explain来了解SQL执行的状态）

2.索引优化  

3.数据库结构优化  

4.服务器硬件优化（ssd、raid）  

5.分表，读写表分离，根据手机号等值模运算分表

6.使用缓存

###七、mysql和nosql的优缺点：（参考：http://www.mamicode.com/info-detail-861022.html）
mysql优点：通用化、技术成熟、 可以进行join等复杂查询；缺点：扩展性差，无法进行分布式存储。

nosql 优点：高并发，支持分布式，易于扩展，可伸缩。      缺点：事务支持较弱、 join等复杂操作能力较弱。
