'''
输入一个正整数，输出其中7的个数，递归实现。

说明：本题是练习递归的，请自觉使用递归实现

输入
一个正整数
输出
其中7的个数
样例输入
76370
样例输出
2
'''
def count_7(s:str,index=0,count:int=0)->int:
    if index==len(s):
        return count
    if s[index]=='7':
        count+=1
    return count_7(s,index+1,count)

print(count_7(input()))