'''
题目描述
编写⼀个程序输入美元转换为人民币的汇率，表示转换方式的数字（0表示将美元转换为人民币；1表示将人民币转换为美元；其他数字则直接输出“Incorrect Input”），以及需要转换的金钱数值，最后将用户输入的美元数或⼈民币数分别转换为⼈民币或美元 (保留一位小数)
输出形式如下：
$100.0 is 681.0 yuan
681.0 yuan is $100.0
输入
6.81 0 100
输出
$100.0 is 681.0 yuan
样例输入
6.81 0 100
样例输出
$100.0 is 681.0 yuan
'''
pyin=eval(input().replace(' ',','))
exchange_rate=pyin[0]
way=pyin[1]
amount=pyin[2]

if way==0:
    print("$%.1f is %.1f yuan" % (amount,amount*exchange_rate))
elif way==1:
    print('{0:.1f} yuan is ${1:.1f}'.format(amount,amount/exchange_rate))
else :
    print('Incorrect Input')