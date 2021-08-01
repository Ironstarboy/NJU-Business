'''
题目描述
键盘输入一组整数（逗号分隔），编写程序对这些数据进行排序（不能直接调用Python中现成的sorted()函数或sort()方法，
自己选择冒泡排序、选择排序、插入排序中的一种算法），输出排序后的数据。

输入
键盘输入逗号间隔的整数
输出
排序后的列表
样例输入
12,34,8,13,21
样例输出
[8, 12, 13, 21, 34]
'''
# nums=eval(input())
nums=[12,34,8,13,21]
def bubble_sort(arr):
    """
    相邻两两比较，大的向右移动
    从小到大
    :param arr:
    :return:
    """
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

    return arr


def select_sort(arr):
    """
    找到后面未排序数组的最小值的索引，值放已排序数组的最后一个
    :param arr:
    :return:
    """
    for i in range(len(arr)):
        min_index=i
        for j in range(i,len(arr)):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[min_index],arr[i]=arr[i],arr[min_index]
    return arr

def insert_sort(arr):
    """
    把后面乱序数组的表头，和以排序的逐个比较
    用链表实现更方便，表头表尾都行，直接移动一连串数组
    :param arr:
    :return:
    """
    for i in range(1,len(arr)):
        for j in range(i,0,-1):
            if arr[j]<arr[j-1]:
                arr[j],arr[j-1]=arr[j-1],arr[j]
    return arr


print(insert_sort(nums))

