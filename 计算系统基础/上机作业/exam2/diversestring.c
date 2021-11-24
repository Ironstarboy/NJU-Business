#include <stdio.h>

int judge_diverse(char *s,int len){
    //法1：递归，如果a[i]diverse a[i+1]diverse就是比a[i]Min少一，或者max大1.递归复杂度目测O(N²)
    //法2：排序，看是否是连续递增 不重复数组
    //hash,mod26，看有没有 连续的，没有碰撞的哈希

    //先产生哈希表
    int hashmap[26]={0};
    int flag=1;
    for(int i=0;i<len;++i){
        int index=s[i]-'a';//三目会报错？
        if(hashmap[index]==0){
            hashmap[index]=1;
        } else{
            flag=0;
        }
    }
    //判断是否连续
    int i=0;
    int j=25;
    while (hashmap[i++]!=1){;}
    while (hashmap[j--]!=1){;}
    i--;j++;
    for(int k=i;k<=j;++k){
        if(hashmap[k]==0){
            flag=0;
        }
    }
    return flag;
}


int main(){
    int n;
    scanf("%d\n",&n);
    int count=0;
    int ans[200];
    int index=0;

    while (count<n){
        char s[51]={'\0'};
        int len=0;
        scanf("%s",s);
        while (s[len++]!='\0'){;}
        len--;
        ans[index++]=judge_diverse(s,len);
        count++;

    }

    //output
//    freopen("test1.txt", "w", stdout);
    for(int i=0;i<index-1;++i){
        if(ans[i]){
            printf("%s\n","Yes");
        } else{
            printf("%s\n","No");
        }
    }
    if(ans[index-1]){
        printf("%s","Yes");
    } else{
        printf("%s","No");
    }
}