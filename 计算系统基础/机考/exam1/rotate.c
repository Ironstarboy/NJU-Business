/*
 * 题目描述
输入一个数组，将数组中的元素向右移动kk个位置后输出。

输入格式
输入包含2行：

第一行包含2个正整数，n，kn，k；nn表示数组的长度,kk表示旋转的次数；
第二行包含一个长度为nn的数组；
输出格式
输出旋转之后的数组。

输入输出样例
输入 #1复制
7 3
1 2 3 4 5 6 7
输出 #1复制
5 6 7 1 2 3 4
 */
#include <stdio.h>
int main(){
    int n,k;
    scanf("%d %d\n",&n,&k);
    int arr[30000]={0};
    int len=0;
    while(1){
        scanf("%d",&arr[len++]);
        if(len==n){
            break;
        }
    }
    int r=len-k%len;
    for(int i=r;i<len;++i){
        printf("%d ",arr[i]);
    }
    for(int i=0;i<r;++i){
        printf("%d ",arr[i]);
    }

}