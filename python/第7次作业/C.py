'''
题目描述
从键盘上读取一个字符串，计算每个字母（按字母表顺序，不区分大小写）出现的次数。
例如字符串“I am a student.”的统计结果为:[2,0,0,1,1,0,0,0,1,0,0,0,1,1, 0,0,0,0,1,2,1,0,0,0,0,0]。
表示字符'A'或'a'共出现了2次，字符'D'或'd'共出现了1次，……依次类推。
输入
由键盘输入一个字符串
输出
输出统计结果
提示

'''
s=input().lower()
letter=list(map(chr,range(ord('a'),ord('z')+1)))
ans=[0]*26
for l in letter:
    ans[letter.index(l)]=s.count(l)
print(ans)