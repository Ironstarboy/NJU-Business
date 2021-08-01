'''
题目描述
求矩阵的两对角线上的元素之和
输入
矩阵的行数N
和一个N*N的整数矩阵a[N][N](N<=10)，整数没有规律，可以是任意整数
输出
所输矩阵的两对角线上的元素之和
样例输入
3
1 2 3
4 5 6
7 8 9
样例输出
25
提示

输入数据可使用的一种思路：


n = 输入行数


for i in range(n):
'''
n=int(input())

mat=[]
for i in range(n):
    arr=eval(input().replace(' ',','))
    mat.append(arr)

if n==1:
    print(mat[0])
else:
    total=0
    N=len(mat)
    for i in range(N):
        total+=mat[i][i] # 主对角线
        for j in range(N):
            if(i+j==N-1):  # 索引和为n-1
                total+=mat[i][j]  # 副对角线

    # 奇数维度矩阵去除重复计数的
    if N%2:
        total-=mat[N//2][N//2]
    print(total)