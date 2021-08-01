'''
题目描述
输入一个字符串“I like Python very much 2333 because Python is very cute 666.”，判别该
字符串中数字字符和单词的个数，并将第一次出现的 Python 替换成 Luffy 并输
出新字符串。
输入
输出
样例输入
I like Python very much 2333 because Python is very cute 666
样例输出
There are 7 letters in the string.
The count of words is 12.
The replaced string is I like Luffy very much 2333 because Python is very cute 666.
'''
s=input().strip('.')
digit_str= ''.join(filter(lambda x:x.isdigit(), s.split()))
leter_list=list(filter(lambda x:x.isdigit()==False,s.split()))
letter_set=set(leter_list)  # 去除重复字母

print('There are {} letters in the string.'.format(len(digit_str)))
print('The count of words is {}.'.format(len(s.split())))
print('The replaced string is {}.'.format(s.replace('Python','Luffy',1)))
