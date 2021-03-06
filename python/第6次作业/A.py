'''
题目描述
按递增顺序依次列出所有分母为40，分子小于40的最简分数。

输入
输出
分数之间用逗号分开(含最末逗号)

样例输出
1/40,3/40,7/40,9/40,11/40,13/40,17/40,19/40,21/40,23/40,27/40,29/40,31/40,33/40,37/40,39/40,
提示

对分子采用穷举法，利用最大公约数的方法，判断分子与40是否构成真分数。
'''
# 40=2^3*5
print(','.join(map(lambda x:str(x)+r'/40',filter(lambda x:x%2!=0 and x%5!=0,range(1,40))))+',')