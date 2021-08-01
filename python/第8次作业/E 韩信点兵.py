'''
题目描述
相传韩信将军才智过人，从不直接清点自己军队的人数，只要让士兵先后以三人一排，五人一排，七人一排的变换队形，而他每次只掠一眼队伍的排尾就知道总人数了。输入包含多组数据，每组数据包含三个非负整数a，b，c，表示每种队形排尾的人数（a<3,b<5,c<7），输出总人数的最小值（或者报告无解）。已知总人数不小于10，不超过100。
输入
输入包含多组数据，每组一行三个整数a，b，c
输出
输出每行对应的总人数的最小值，若无解则输出“No answer”
样例输入
2 1 6
2 1 3
样例输出
41
No answer
提示
输入一行，输出一行，空行结束

例如：

2 1 6

41

2 1 3

No answer
'''
def hanxin(remainder_list):
    """
    返回士兵数量，返回0即no answer
    :param remainder_list: 余数列表
    :return:
    """
    ans=0
    for i in range(10,100+1):
        if i%3==remainder_list[0] and i%5==remainder_list[1] and i%7==remainder_list[2]:
            ans=i
    return ans



while 1:
    arr=input()
    if arr!='':
        arr = list(map(int, arr.split()))

        num = hanxin(arr)
        if num:
            print(num)
        else:
            print('No answer')
    else:
        break






