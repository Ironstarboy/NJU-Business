/*
 * 题目描述
输入一个长度为n(1<=n<=100)n(1<=n<=100)递增的数组,输出这个数组中没有出现的最小的正整数。

输入格式
输入包含2行：

第一行包含一个正整数nn，表示数组的长度；
第二行包含一个长度为nn的数组；
输出格式
输出包含1行，结果是一个正整数，表示该数组中没有出现的最小的正整数。

输入输出样例
输入 #1复制
5
1 2 4 5 6
输出 #1复制
3
输入 #2复制
5
1001 1002 15634 36548 40000
输出 #2复制
1
说明/提示
1=<n<=1001=<n<=100

1<=a_{i}<=10^{6}1<=a
i <=10 ^6
 */
#include <stdio.h>

int isInList(int target,int num[],int len){
    int flag=0;
    for(int i=0;i<len;++i){
        if(num[i]==target){
            flag=1;
            break;
        }
    }
    return flag;
}
int main(){
    int n;
    scanf("%d\n",&n);
    int num[100]={0};
    int len=0;
    for(int i=0;i<n;++i){
        scanf("%d",&num[len++]);
    }
    int max_num=num[len-1]+1;

    int isout=0;
    for(int i=1;i<max_num;++i){
        if(!isInList(i,num,len)){
            printf("%d",i);
            isout=1;
            break;

        }
    }
    if(!isout){
        printf("%d",num[len-1]+1);
    }
}