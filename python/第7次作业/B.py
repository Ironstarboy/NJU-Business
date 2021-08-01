'''
题目描述
用1,2,3...9组成三个三位数abc，def，ghi，每个数字恰好使用一次，要求abc：def：ghi=1:2:3.按照“abc def ghi”的格式输出所有解，每行一个。
输入
无
输出
输出符合要求的“abc def ghi”，每行一个，每一行的3个数要求按照从小到大的顺序输出。
样例输出
192 384 576
219 438 657
273 546 819
327 654 981
'''
# C9 3 C 63 C 33
nums=list(range(1,10))


def all_different(num):
    """
    判断数字里是否全部相同,且都是1-9
    :param num: 多位数字,int
    :return:
    """
    num_str=str(num)
    for i in num_str:
        if num_str.count(i)>1 or '0' in num_str:
            return False
    return True

ans=[]
for i in range(123,334):
    if all_different(i):
        j=i*2
        if all_different(''.join(map(str,[i,j]))):
            k=i*3
            if all_different(''.join(map(str,[i,j,k]))):
                ans.append([i,j,k])
print('\n'.join(map(lambda x:' '.join(map(str,x)),ans)))