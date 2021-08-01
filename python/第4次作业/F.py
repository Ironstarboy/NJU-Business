'''
题目描述
输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。
输入
输入是一行，有多个整数，每个整数之间用空格隔开。
输出
输出元素交换过的列表。
样例输入
1 2 3 7 9 8
样例输出
[9, 2, 3, 7, 8, 1]
'''
nums=list(eval(input().replace(' ',',')))
max_index=nums.index(max(nums))
min_index=nums.index(min(nums))
nums[-1],nums[min_index]=nums[min_index],nums[-1]
nums[0],nums[max_index]=nums[max_index],nums[0]

print(nums)