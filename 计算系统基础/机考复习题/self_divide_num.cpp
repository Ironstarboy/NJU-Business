/*
 *
 * 题⽬描述
⾃除数 是指可以被它包含的每⼀位数除尽的⾃然数。
同时，⾃除数不包含 0 ，或者其中有某⼀位数字为0的数字。
还有，⾃除数不允许包含 0 。
给定⼀个数，请编写代码，判断某个数字是否为⾃除数
输⼊描述
输⼊包括⼀个整数，即给定的需要判断的⾃然数
输出描述
输出是⼀个字符串，即true 或 false，表明给定输⼊数是否为⾃除数
测试样例
样例1: 输⼊-输出-解释
128
true
 解释：128 是⼀个⾃除数，因为 128 % 1 == 0，128 % 2 == 0，128 % 8 == 0。
 */
# include <stdio.h>
# include <math.h>
int main(){
    //读取
    const int size=100;
    char num[size];
    int index=0;
    while(1){
        num[index++]=getchar();
        if(num[index-1]=='\n'){
            break;
        }
    }


    //char[]转INt
    int n=0;
    for(int i=0;i<index-1;++i){
        n+=(num[i]-'0')*pow(10,index-2-i);
    }

    //判断
    int flag=1;
    for(int i=0;i<index-1;++i){
        if(num[i]=='0'){
            flag=0;
            break;
        }
        if(n%(num[i]-'0')!=0){
            flag=0;
            break;
        }
    }


    //输出
    if(flag){
        printf_s("true");
    }
    else{
        printf_s("false");
    }
}
