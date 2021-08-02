2021夏季：

均分73，几乎不会挂人，会海底捞

最高分98，课程设计扣2分，期中期末满分

# 第一部分 填空

1. 以下代码输出几行？

~~~python
try:
    a=eval('6/2')
    print(a)
    b=int(6/2)
    print(b)
    c=int('6/2')
    print(c)
except Exception as e:
    print('wrong')
else:
    print('yes')
~~~



2. 输出结果是：

~~~python
n=4
mat=[[0]*n for i in range(n)]
k=1
for i in range(n):
    if i%2==0:
        for j in range(n):
            mat[i][j]=k
            k+=1
    else:
        for j in range(n-1,-1,-1):
            mat[i][j]=k
            k+=1

print(mat[2][1])
~~~
3. 输出结果是：

~~~python

def f(n):
    if n==1:
        return [1]
    else:
        lst=[i for i in range(1,n+1)]
        return f(n-1)+lst
a=f(3)
print(a)
~~~

4. 输出是:

~~~python
   class person:
       counter=0
       def __init__(self,name,age):
           self.name=name
           self.age=age
           person.counter+=1
       def introduce(self):
           print('{} is No{}.'.format(self.name,person.counter))
   
   class student(person):
       def learn(self,hours):
           print('{} studies {} hours everyday'.format(self.name,hours))
   
   stu1=student('Qiangqiang',20)
   stu1.introduce()
   stu1.learn(8)
   stu2=student('Huahua',18)
   stu2.introduce()
   stu2.learn(12)
~~~

   5. 输出是:


~~~python

class Animal:
    count=0
    def __init__(self,name):
        self.name=name
        Animal.count+=1

class Cat(Animal):
    def __init__(self,name):
        super().__init__(name)
    def call(self):
        print('cat {} {}'.format(self.name,Animal.count))

class Dog(Animal):
    def __init__(self,name):
        super().__init__(name)
        self.count+=1
    def call(self):
        print('dog {} {}'.format(self.name,self.count))


cat=Cat('shufen')
cat.call()
dog=Dog('xigua')
dog.call()
~~~

# 改错

1. 具体代码忘了

```python
# 改错题：奇怪的for else结构，用Break居然能阻止else运行。原理是for被break中断，会执行else语句
for i in range(10):
    if i==1:
        print(i)
        break
else:
    print('else')
```

2. 考了matplotlib绘图，由于第三方库的方法太多记不住，考试有时候会考很偏的，考试遇到直接help查看文档

# 程序编写

要求写一个处理文件的函数