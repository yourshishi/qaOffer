#一、打印指定行：
    awk  "NR==10"  file.txt 

#二、统计
1、使用命令行计算日志中的服务qps：
      [2017-04-25 15:31:11] service /ser1/cancel - - 175.57.2.66 77 94 0 0 -
      [2017-04-25 16:31:11] service /ser1/delete - - 175.57.2.67 77 94 0 0 -
       cat qps.txt | grep cancel  | awk -F ']'  '{print $1}' | cut -d ":" -f 3 | sort -n | uniq -c 
      tail -f :取增量       grep ：取出cancel这个服务
      -F : awk脚本编辑器中设定分隔符awk -F ']'  '{print $1}' ，上述命令取出时间[2017-04-25 15:31:11。
      cut -d ':' -f 3 取出按分号分割后的第三列即取出秒。   uniq -c: 去重取计数

2、写一个shell脚本进行access.log日志统计,得到访问ip最多的前10个:
      10.90.183.57 -- [21/Mar] "GET /qmonitor"
      cat  access.log | awk -F '--' '{print $1}' | cut -d 

3、统计文章中出现top10的单词及次数
     cat qps.log | sort | uniq -c | sort -k 1,1nr | head  -10

#三、如果进程在，就杀掉进程：
     kill -9 `ps -ef|grep "java"|grep -v "grep"|awk '{print $2} '`

#四、在每行的头添加字符，
比如"HEAD"，命令如下：
sed 's/^/HEAD&/g' test.file
在每行的行尾添加字符，比如“TAIL”，命令如下：
sed 's/$/&TAIL/g' test.file
1."^"代表行首，"$"代表行尾
2.'s/$/&TAIL/g'中的字符g代表每行出现的字符全部替换，如果想在特定字符处添加，g就有用了，否则只会替换每行第一个，而不继续往后找了。

#五、查找端口8899端口占用情况:
     netstat -a | grep 8899
     lsof -i:8899

#六、修改当前路径下的tools文件夹的所有者为tomcat:
     chown -R tomcat tools/

#七、网络
1）查看系统当前网络连接数
netstat -n | awk '/^tcp/ {++S[$NF]} END {for(a in S) print a, S[a]}'

2）查看堆内对象的分布 Top 50（定位内存泄漏）
jmap –histo:live $pid | sort-n -r -k2 | head-n 50

3）按照 CPU/内存的使用情况列出前10 的进程
内存  ps axo %mem,pid,euser,cmd | sort -nr | head -10
CPU  ps -aeo pcpu,user,pid,cmd | sort -nr | head -10

4）显示系统整体的 CPU利用率和闲置率
grep "cpu " /proc/stat | awk -F ' ' '{total = $2 + $3 + $4 + $5} END {print "idle \t used\n" $5*100/total "% " $2*100/total "%"}'

5）按线程状态统计线程数(加强版)
jstack $pid | grep java.lang.Thread.State:|sort|uniq -c | awk '{sum+=$1; split($0,a,":");gsub(/^[ \t]+|[ \t]+$/, "", a[2]);printf "%s: %s\n", a[2], $1}; END {printf "TOTAL: %s",sum}';

6）查看最消耗 CPU 的 Top10 线程机器堆栈信息
推荐大家使用 show-busy-java-threads 脚本，该脚本可用于快速排查 Java 的 CPU 性能问题(top us值过高)，自动查出运行的 Java 进程中消耗 CPU 多的线程，并打印出其线程栈，从而确定导致性能问题的方法调用，该脚本已经用于阿里线上运维环境。链接地址：https://github.com/oldratlee/useful-scripts/。

7）火焰图生成（需要安装 perf、perf-map-agent、FlameGraph 这三个项目）：
1. 收集应用运行时的堆栈和符号表信息（采样时间30秒，每秒99个事件）；
       sudo perf record -F 99 -p $pid -g -- sleep 30; ./jmaps
2. 使用 perf script 生成分析结果，生成的 flamegraph.svg 文件就是火焰图。
       sudo perf script | ./pkgsplit-perf.pl | grep java | ./flamegraph.pl > flamegraph.svg

8）按照 Swap 分区的使用情况列出前 10 的进程
for file in /proc/*/status ; do awk '/VmSwap|Name|^Pid/{printf $2 " " $3}END{ print ""}' $file; done | sort -k 3 -n -r | head -10

9）JVM 内存使用及垃圾回收状态统计
显示最后一次或当前正在发生的垃圾收集的诱发原因jstat -gccause $pid
显示各个代的容量及使用情况jstat -gccapacity $pid
显示新生代容量及使用情况jstat -gcnewcapacity $pid
显示老年代容量jstat -gcoldcapacity $pid
显示垃圾收集信息（间隔1秒持续输出）jstat -gcutil $pid 1000

10）其他的一些日常命令
快速杀死所有的 java 进程 ps aux | grep java | awk '{ print $2 }' | xargs kill -9
查找/目录下占用磁盘空间最大的top10文件find / -type f -print0 | xargs -0 du -h | sort -rh | head -n 10
