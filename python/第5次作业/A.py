'''
题目描述
斐波纳契数列

1，1，2，3，5，8，13，21，34，55，89……这个数列则称为“斐波纳契数列”，其中每个数字都是“斐波纳契数”。

输入
输入一个整数N（N不大于40）
输出
由N个“斐波纳契数”组成的“斐波纳契数列”。空格间隔，最后一个数后面没有空格
样例输入
6
样例输出
1 1 2 3 5 8
'''
number=int(input())

def fib(num:'int>=2',ans:list,index:int=0):
    if index<num-2:
        ans.append(ans[index] + ans[index + 1])
        index += 1
        return fib(num,ans,index)
    return
ans=[1,1]
if number==1:
    print(1)
else:
    fib(number,ans)
    print(' '.join(map(str,ans)))