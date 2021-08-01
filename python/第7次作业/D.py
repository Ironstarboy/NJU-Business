'''
题目描述
输入一组正整数（逗号间隔），寻找其中的平方数，
将这些平方数的素因子去重后按从小到大的顺序输出（逗号间隔，最后一个数后面没有逗号）。
输入
输入一组正整数（逗号间隔）
输出
按从小到大的顺序的去重后的素因子（逗号间隔，最后一个数后面没有逗号）
样例输入
60,17,144,49
样例输出
2,3,7
'''
nums=eval(input())

def is_prime(num):
    # 判断是否是素数的函数
    # 返回值
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True

def find_prime_factors(num):
    # 寻找数字num所有的因子
    prime_factors=[]
    for i in range(2,int(num**0.5)+1):
        if num%i==0  and is_prime(i):# 如果num整除i，则i是num的因子。同时判断是否是素数
            prime_factors.append(i)
    return prime_factors # num的素因子存在列表里

total_prime_factors=[]  # 4个数的所有素因子
for i in nums:
    if int(i**0.5)**2==i:  # 筛选出平方数i
        total_prime_factors.extend(find_prime_factors(i))
print(','.join(map(str,sorted(total_prime_factors))))
