'''
题目描述
中国古代数学著作《算经》中提出一个问题：公鸡每只5钱，母鸡每只3钱，小鸡1钱3只。若用100钱买100只鸡（每种鸡必须都买到），输出所有的买法，要求输出结果形式如“rooster=公鸡只数,hen=母鸡只数,chick=小鸡只数”，并且按公鸡只数由小到大的顺序输出，有多组解时分行输出。
输入
输出
样例输出
格式如下：
rooster=1,hen=2,chick=3
rooster=2,hen=3,chick=4
...
提示
'''
rooster_price=5
hen_price=3
chick_price=1/3
count=0
out=[]
for rooster_amount in range(1,100//rooster_price+1):
    for hen_amount in range(1,100//hen_price+1):
        chick_amount=100-rooster_amount-hen_amount
        if chick_amount>=1 and chick_amount*chick_price+rooster_amount*rooster_price+hen_amount*hen_price==100:
            count+=1
            out.append([rooster_amount,hen_amount,chick_amount])

res=sorted(out,key=lambda x:(x[0],x[1],x[2]))
for i in res:
    print('rooster={},hen={},chick={}'.format(i[0],i[1],i[2]))
# print(count)