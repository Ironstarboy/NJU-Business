'''
题目描述
自行建立一个月份与天数的字典monthdays，月份为‘Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Thi',对应的天数为31，28，31，30，31，30，31，31，30，31，40。

按顺序完成以下问题：

（1）创建一个新的字典x = {'Nov':30,'Dec':31}，并将其包含的键值对追加到字典monthdays里。

（2）删除键为’Thi’的键值对。
（3）按照ASCII码顺序，输出字典monthdays的键序列。
（4）按大小排序显示字典monthdays的值序列。（从小到大）
（5）按照字典的键排序，显示字典monthdays的键值对序列。
（6）获取键‘Mar'对应的值。
（7）获取键’Abc'对应的值，没有则显示'No Found!'。
（8）修改键‘Feb'的值为29，并输出该值。
以行的方式输出每一道小题的答案。
输入
输出
['Apr', 'Aug', 'Dec', 'Feb', 'Jan', 'Jul', 'Jun', 'Mar', 'May', 'Nov', 'Oct', 'Sep']
[28, 30, 30, 30, 30, 31, 31, 31, 31, 31, 31, 31]
[('Apr', 30), ('Aug', 31), ('Dec', 31), ('Feb', 28), ('Jan', 31), ('Jul', 31), ('Jun', 30), ('Mar', 31), ('May', 31), ('Nov', 30), ('Oct', 31), ('Sep', 30)]
31
No Found!
29
提示
按照字典的键排序，可使用
sorted(monthdays.items(),key = lambda d:d[0])z
'''
month=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Thi']
days=eval('31，28，31，30，31，30，31，31，30，31，40'.replace('，',','))
monthdays=dict(zip(month,days))
# （1）创建一个新的字典x = {'Nov':30,'Dec':31}，并将其包含的键值对追加到字典monthdays里。
x={'Nov':30,'Dec':31}
monthdays.update(x)

# （2）删除键为’Thi’的键值对。
monthdays.pop('Thi')

# （3）按照ASCII码顺序，输出字典monthdays的键序列。
print(sorted(monthdays.keys()))

# （4）按大小排序显示字典monthdays的值序列。（从小到大）
print(sorted(monthdays.values()))

# 5）按照字典的键排序，显示字典monthdays的键值对序列。
print(sorted(monthdays.items()))

# 6）获取键‘Mar'对应的值。
print(monthdays.get('Mar'))
# print(monthdays['Mar'])

# 7）获取键’Abc'对应的值，没有则显示'No Found!'。
val=monthdays.get('Abc')  # 没有返回None
if val:
    print(val)
else:
    print('No Found!')
# print(monthdays['Abc'])  # 返回KeyError

# 8）修改键‘Feb'的值为29，并输出该值。
monthdays['Feb']=29
print(monthdays.get('Feb'))