s=input('输入字符串：\n').lower()
count=0
for i in s:
    if i=='a':
        count+=1
print('a出现{}次'.format(count))

