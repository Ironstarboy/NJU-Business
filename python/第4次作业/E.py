'''
题目描述
编写一个输入分数，输出分数等级的程序，具体为：

90~100 A

70~89  B

60~69  C

0~59   D

others  Invalid score

注意：输入的分数如果是0~100内的全数字字符串则有相对应的等级，其它输入都为非法输入（比如含有字母或标点符号的字符串）

输入
70
输出
B
样例输入
90
样例输出
A
'''
score_str=input()
if score_str.isdigit():
    score=int(score_str)
    if 90<=score<=100:
        print('A')
    if 70<=score<=89:
        print('B')
    if 60<=score<=69:
        print('C')
    if 0<=score<=59:
        print('D')
else:
    print('Invalid score')