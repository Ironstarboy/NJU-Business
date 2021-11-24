/*
 * 小蓝鲸最近在练习英语听力，他觉得根据听到的英文写出数字非常困难，于是他购买了AI学习机，他将一串数字输入到AI学习机中，AI学习机就会立刻显示这个数字的英文表达。请你模拟一下这个AI学习机的功能。

题目描述
输入一个正整数nn，输出这个正整数的英文表达。

输入格式
输入包括一行:

一个正整数nn
输出格式
输出包括一行：

表示这个正整数的英文表达(不需要and)。
注意：各个英文单词的首字母要大写，两个英文单词之间用空格隔开(末尾没有空格！)
 输入输出样例
输入 #1复制
1
输出 #1复制
One
输入 #2复制
2134
输出 #2复制
Two Thousand One Hundred Thirty Four
输入 #3复制
1234567
输出 #3复制
One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven
输入 #4复制
1234567891
输出 #4复制
One Billion Two Hundred Thirty Four Million Five Hu
 1<=n<=2 ^31 −1
 */
#include <stdio.h>
#include <malloc.h>
char *my_strcat(char *a, char *b) {
    char *c = (char *) malloc(20*sizeof(char)); //局部变量，用malloc申请内存
    char *tempc = c; //把首地址存下来
    while (*a != '\0') {
        *c++ = *a++;
    }
    while ((*c++ = *b++) != '\0') {
        ;
    }
    //注意，此时指针c已经指向拼接之后的字符串的结尾'\0' !
    return tempc;//返回值是局部malloc申请的指针变量，需在函数调用结束后free之
}


char* onesdigit2en(int num){
    //个位数翻译
    switch (num) {
        case 0:return my_strcat("","");
        case 1:return my_strcat("One","");
        case 2:return my_strcat("Two","");
        case 3:return my_strcat("Three","");
        case 4:return my_strcat("Four","");
        case 5:return my_strcat("Five","");
        case 6:return my_strcat("Six","");
        case 7:return my_strcat("Seven","");
        case 8:return my_strcat("Eight","");
        case 9:return my_strcat("Nine","");
        default:return my_strcat("","");//不写defalut直接RE
    }
}


char* tensdigit2en(int num1,int num2){
    //2位数翻译,[10,19]需要特别翻译
    char *temp="";
    switch (num1) {
        case 1:
            switch (num2) {
                case 0:return my_strcat("Ten","");
                case 1:return my_strcat("Eleven","");
                case 2:return my_strcat("Twelve","");
                case 3:return my_strcat("Thirteen","");
                case 4:return my_strcat("Fourteen","");
                case 5:return my_strcat("Fifteen","");
                case 6:return my_strcat("Sixteen","");
                case 7:return my_strcat("Seventeen","");
                case 8:return my_strcat("Eighteen","");
                case 9:return my_strcat("Nineteen","");
                default:return my_strcat("","");
            }
            break;
            //"s"在常量区
        case 2:temp="Twenty ";break;
        case 3:temp="Thirty ";break;
        case 4:temp="Forty ";break;
        case 5:temp="Fifty ";break;
        case 6:temp="Sixty ";break;
        case 7:temp="Seventy ";break;
        case 8:temp="Eighty ";break;
        case 9:temp="Ninty ";break;
        case 0:temp="";break;
        default:temp="";break;
    }
    char* ans= my_strcat(temp, onesdigit2en(num2));//用自定义strcat，每次都开辟新地址
    return ans;
}


void  right_just(char *s,char filler,int strlen,char* out){
    //strlen 数字的位数
    for(int i=0;i<10-strlen;++i){
        out[i]=filler;
    }
    int index=0;
    for(int i=10-strlen;i<10;++i){
        out[i]=s[index++];
    }
    out[10]='\0';
}
int main(){

    char num[11]={'\0'};//剩余 自动'\0'
    //多开一位存'\0'
    //最大数字2147483647 10位数
    int len=0;
    scanf("%s",&num);
    while (num[len++]!='\0'){;}
    len--;

    char just_num[11]="";//用*just_num会RE

    right_just(num,'0',len,just_num);


    int b1=just_num[0]-'0';
    if(b1!=0){
        printf("%s Billion ",onesdigit2en(b1));
    }
    //每次处理3位
    for(int i=1;i<10;i=i+3){
        int n1=just_num[i]-'0';
        int n2=just_num[i+1]-'0';
        int n3=just_num[i+2]-'0';
        if(n1|n2|n3!=0){
            if(n1!=0){
                printf("%s Hundred ",onesdigit2en(n1));
            }
            char* temp=tensdigit2en(n2,n3);

            printf("%s ",temp);
//            free(temp);//释放分配的指针
            switch (i) {
                case 1:printf("%s ","Million");
                    break;//不加break,case匹配成功后，继续向下执行
                case 4:printf("%s ","Thousand");
                    break;
                default:;
            }
        }

    }

}
