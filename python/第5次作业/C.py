'''
题目描述
输入n(n<=100)个整数，按照绝对值从大到小排序后输出。题目保证对于每一个测试实例，所有的数的绝对值都不相等。
输入
首先输入一个整数代表有多少组，每组占一行，每行有若干个整数用空格彼此隔开
输出
对于每个每行的测试实例，输出排序后的结果，两个数之间用一个空格隔开（注意每行最后一个数的结尾也有空格）。每个测试实例占一行
样例输入
2
3 -4 2
0 1 2 -3
样例输出
-4 3 2
-3 2 1 0
'''


def absolute_select_rank(arr):
    """
    从小到大,从i-n,选最小值与i-1交换
    :param arr:
    :return:
    """

    for i in range(len(arr)):
        min_num_index = i
        for j in range(i + 1, len(arr)):
            a=abs(arr[j])
            b=abs(arr[min_num_index])
            if abs(arr[j]) > abs(arr[min_num_index]):
                min_num_index = j
        arr[i], arr[min_num_index] = arr[min_num_index], arr[i]
    return arr


rows=int(input())
row_count=0
nums=[]
while row_count<rows:
    row_count+=1
    numbers=list(eval(input().replace(' ',',')))
    sorted_numbers=absolute_select_rank(numbers)
    nums.append(sorted_numbers)

for lst in nums:
    print(' '.join(map(str,lst)))




