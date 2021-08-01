'''
题目描述

素数有很多神奇的性质，所以很美。我们知道一个日期将年、月、日按顺序连接在一起可以组成一个八位数，例如2011年3月6日可以写成20110306。我的某个MM的生日组成的数是一个素数。偶尔我叫她素MM，没人知道是啥意思，她自己也不知道。O(∩_∩)O哈哈~我心里可是真的美美的(⊙o⊙)哦！

嗯，什么？你的生日也是素数？你也想做“素MM”或者“素GG”？那好吧，不过我可是很小气的哦！只有你出生在1988年或者1989年我才让你做“素MM”或“素GG”。要不然，你把这两年里日期组成的数是素数的找出来也可以.

输入

无

输出

1988年与1989年，这两年里的日期所组成的素数。每个素数占一行（用换行符输出，最后一行不需要退格处理）。

样例输出
19880101
19880111
19880117
19880129
19880221
……
'''
def isp(x):
    if x==1:
        return False
    k=int(x*0.5)
    for j in range(2,k+1):
        if x%j==0:
            return False
    return True
lst=[]
for i in range(1,13):
    if i in [1,3,5,7,8,10,12]:
        for k in range(1,32):
           a=1988*10000+i*100+k
           if isp(a):
               lst.append(a)
    elif  i in [4,6,9,11]:
        for k in range(1,31):
            a=1988*10000+i*100+k
            if isp(a):
               lst.append(a)
    else:
        for k in range(1,30):
            a=1988*10000+200+k
            if isp(a):
                lst.append(a)

for i in range(1,13):
    if i in [1,3,5,7,8,10,12]:
        for k in range(1,32):
           a=1989*10000+i*100+k
           if isp(a):
               lst.append(a)
    elif  i in [4,6,9,11]:
        for k in range(1,30):
            a=1989*10000+i*100+k
            if isp(a):
               lst.append(a)
    elif i==2:
        for k in range(1,29):
           a=1989*10000+i*100+k
           if isp(a):
               lst.append(a)
for i in lst:
    print(i)