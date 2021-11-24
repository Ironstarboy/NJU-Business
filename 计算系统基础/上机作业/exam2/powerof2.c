/*
 * 题目描述
输入一个非负整数nn，请你计算2^n2
n
输入格式
输入包括一行：

一个非负整数nn，表示2的幂次。
输出格式
输出包括一行：

表示2^n2 n
 。
输入输出样例
输入 #1复制
2
输出 #1复制
4
输入 #2复制
3
输出 #2复制
8
说明/提示
0<=n<=1000000
 */
# include <stdio.h>
void mul(int*a ,int b,int *len){
    //a*b a为大数 b为【0，9】len为a的有效数字部分（即a是几位数）
    int temp;
    int carry=0;
    int i=0;
    //a逆序表示，a[0]个位 a[1]十位...
    for(i=0;i<*len;++i){
        temp=a[i]*b+carry;
        a[i]=temp%10;
        carry=temp/10;
    }
    while(carry!=0){
        a[i]=carry%10;
        carry=carry/10;
        i++;
    }
//    printf("%d",i);
    *len=i;
}

int main(){
    int n;
    scanf("%d",&n);
    int arr[100002]={1};
    for(int i=1;i<100002;++i) {
        arr[i]=0;
    }
    int len=1;
    int *p=&len;

    while (n){
        mul(arr,2,p);
        n--;
    }

    //逆序输出
    for(int i=len-1;i>=0;--i){
        printf("%d",arr[i]);
    }

}