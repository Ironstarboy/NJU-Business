'''
题目描述
列表中存放了n个整数，分别表示n个评委的评分，请编写程序，去掉其中的最高分和最低分，求剩下n-2个分数的平均值(保留两位小数)。
输入
35, 78, 91, 35, 20, 10, 20, 80, 10, 90, 80, 10, 25, 35, 56, 72, 98, 43, 10, 38
输出
46.00
'''
nums_str=input().split(',')
nums=list(map(int,nums_str))
nums.remove(max(nums))
nums.remove(min(nums))
print("{0:.2f}".format(sum(nums)/len(nums)))