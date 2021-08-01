'''
题目描述
有 5 个好朋友小明、 阿花、 大壮、 大毛和小毛， 他们的 QQ 号分别是 88888、 5555555、11111、 1234321 和 1212121， 用字典将这些数据组织起来， 实现如下程序功能：
（1）定义函数 find_QQ()， 功能是根据主调函数传入的存放姓名和对应 qq 号的字典及某一个人的姓名（形参）在字典中查找对应的 QQ 号， 若找到则返回该 QQ 号， 若找不到则返回 None；
（2）在__main__模块中输入（利用input()函数，数据由系统自动输入）一个包含 5 个好朋友姓名和对应 QQ 号的字典， 输入要查询的姓名调用 find_QQ()函数， 如果找到则输出该 QQ 号， 如果输入的姓名不在字典中则给出提示信息允许再次输入并调用 find_QQ()函数查询， 如果输入 3 次仍未找到则结束查询。

输入
程序首先输入一个整数n，代表总共有n个人。接下来有n行，每行表示一个人的姓名和对应的QQ号，中间用一个空格隔开。

至此，相关数据已经输入完毕。接下来是查询过程的输入，输入需要查询QQ号的姓名，如果此姓名不存在则继续输入直到3次为止，若存在则输出对应的QQ号并结束查询。

输出
在查询过程中我们使用如下提示信息要求用户输入姓名：

"Please enter the name: "

如果不存在则如下提示重新输入：

"Enter the name again: "

如果输入了3次（包括第1次输入）还未输入正确则输出：

"Bye!"终止输入查询。

如果用户输入的姓名存在则输出对应的QQ号，像下面这样：

"The QQ number of name is: QQnumber"

其中name是用户输入的姓名，QQnumber是其QQ号。

样例输出

提示

 输入参考：

输入n的值：

n=int(input())

读入多个字符串：

for i in range(n):

    line=input().split()

    处理


注意：input()函数的提示字符串中冒号后有一个空格。

'''


def find_QQ(dic,name):
    return dic.get(name)

def write_data():
    name_lst=[]
    QQ_num=[]
    n=int(input())
    for i in range(n):
        name_QQ=input().strip().split()
        name_lst.append(name_QQ[0])
        QQ_num.append(name_QQ[1])
    return dict(zip(name_lst,QQ_num))

if __name__=='__main__':
    name_QQ_dic=write_data()
    count=1
    name=input("Please enter the name: ")
    while 1:

        QQ=find_QQ(name_QQ_dic,name)
        if QQ is None:
            name=input("Enter the name again: ")
            count+=1
        QQ = find_QQ(name_QQ_dic, name)
        if QQ is not None:
            print("The QQ number of {} is: {}".format(name,QQ))
            break
        if count>=3:
            print('Bye!')
            break
