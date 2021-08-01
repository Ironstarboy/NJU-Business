'''
题目描述
不使用标准模块的函数，采用递推法计算sinx幂级数展开式的近似值，当通项绝对值小于10-8时停止累加，保留1位小数。
sinx=x/1-x3/3!+x5/5!-x7/7!…

输入
在程序中用x = float(input())表示输入，x由系统自动输入（无需人工输入）
输出
样例输入
3.1415926
样例输出
0.0
提示
'''
x=float(input())
eps=1e-8  # 精度
sinx=x


count=1
sign_flag=-1
x_temp=x
while(abs(x)>eps):
    count += 1
    x=x*x_temp*x_temp/(2*count-2)/(2*count-1)
    sinx +=sign_flag*x
    sign_flag *= -1

print('{0:.1f}'.format(sinx))