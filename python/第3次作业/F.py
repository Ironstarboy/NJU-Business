'''
题目描述
列表中存放了某次考试学生的考试成绩，请编写程序分别求出不及格学生和甲等（大于85）学生的平均成绩。（数据中肯定存在各一名成绩为85和60的学生，并且每位学生的成绩都不一样，结果分行输出且保留两位小数）
输入
85,55,93,75,56,47,67,90,24,88,60
输出
45.50

90.33
样例输入
85,55,93,75,56,47,67,90,24,88,60
样例输出
45.50
90.33
提示
'''
# scores_str=input().split(',')# 用split谜之错误，助教也不懂
# scores=[eval(i) for i in scores_str]

scores=list(eval(input()))

unpass=list(filter(lambda x:x<60,scores))
excellence=list(filter(lambda x:x>85,scores))
if len(unpass)>0:
    print("{0:.2f}".format(sum(unpass)/len(unpass)))
if len(excellence)>0:
    print("{0:.2f}".format(sum(excellence)/len(excellence)),end='')
