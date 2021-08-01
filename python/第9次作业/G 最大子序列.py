'''
输入一个正整数n和长度m，寻找将n中所有长度不超过m的子序列转成的整数中的最大值。

例如正整数2835，长度不超过2的子序列有2、8、3、5、28、23、25、83、85、35，其中转换为整数的最大值是85。

输入
两行，第一行是正整数n，第二行是长度m
输出
长度不超过m的子序列转成的整数中的最大值
样例输入
2835
2
样例输出
85
提示
考虑是否使用n的个位数，如果不使用n的个位数，那么结果是n//10的长度不超过m的最大子序列，如果使用n的个位数，那么结果又是多少？在这两个结果中返回较大的那个。
'''
def permutation(s, ans:list, start:int=0):
    if start==len(s)-1:
        ans.append(s)
    for i in range(start,len(s)):
        s[i],s[start]=s[start],s[i]
        s_new=s.copy()
        permutation(s_new, ans, start + 1)
        s[i], s[start] = s[start], s[i]



def sub_seq(seq,m):
    global ans
    max_sub_seq_len=len(ans[-1][0])  # 子序列的最长长度
    if max_sub_seq_len==m:
        return
    out=[]
    for s in ans[-1]:
        for i in seq:
            if seq.index(s[-1])<seq.index(i):
                temp=s+i
                out.append(temp)
    ans.append(out)
    sub_seq(seq,m)

def my_bin(n,m):
    '''
    00000这种，n是位数，m是有几个1
    :param n:
    :param m:
    :return:
    '''
    out=[]
    for i in range(1,2**(n)):
        temp='{0:0>{1:}}'.format(bin(i)[2:],n)
        if temp.count('1')==m:
            out.append(temp)
    return out

n=list(input())  # 整数
m=int(input())  # 子序列长度
# n='2385'
# m=2
indexs=[]
for i in range(1,m+1):
    indexs.append(my_bin(len(n),i))

out=[]
for lst in indexs:
    for s in lst:
        temp=''
        for j in range(len(s)):
            if s[j]=='1':
                temp+=n[j]
        if temp!='':
            out.append(int(temp))
print(max(out))
# ans=[n]  # 二维列表，存着子序列长度为1，2，3..的列表
# sub_seq(n,m)

# 将ans里的数字变为整数,存到新列表
# out=[]
# for lst in ans:
#     for num in lst:
#         out.append(int(num))
#
# print(max(out))


