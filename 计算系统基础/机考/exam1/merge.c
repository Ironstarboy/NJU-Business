/*
 * 题目描述
给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，

请你 把 nums1 和 nums2 合并成一个数组，使合并后的数组同样按 递增顺序 排列

输入格式
输入包含3行：

第1行包含两个整数n,mn,m,分别表示nums1和nums2的长度
第2行是长度为nn的num1;
第3行是长度为mm的nums2；
输出格式
输出归并后的数组。

输入输出样例
输入 #1复制
3 3
1 2 3
2 5 6
输出 #1复制
1 2 3 5 6
输入 #2复制
3 4
1 2 3
2 3 4 5
输出 #2复制
1 2 3 4 5
说明/提示
0 <= m, n <= 2000<=m,n<=200

1 <= m + n <= 4001<=m+n<=400

-10^{9} <= nums1[i], nums2[j] <= 10^{9}−10
9
 <=nums1[i],nums2[j]<=10
9
 */
# include <stdio.h>
int main(){

    int n,m;
    scanf("%d %d\n",&n,&m);

    if(n==0 || m==0){
        int arr[200]={0};
        int len=0;
        while(1){
            scanf("%d",&arr[len++]);
            if(len==n || len==m){
                break;
            }
        }
        int idx=1;
        int ans[500];//存放不重复元素的数组
        ans[0] = arr[0];
        for(int i=1;i<500;i++){
            if(arr[i] != arr[i-1]){//如果当前遍历的元素和前一个元素不相等
                ans[idx++] = arr[i];
            }
        }
        idx--;
        for(int i=0; i < len; i++){
            printf("%d ", ans[i]);
        }
        return 0;
    }

    int arr1[220]={0};
    int arr2[220]={0};

    int len1=0;
    int len2=0;
    while(1){
        scanf("%d",&arr1[len1++]);
        if(len1==n){
            break;
        }
    }
    while (1){
        scanf("%d",&arr2[len2++]);
        if(len2==m){
            break;
        }
    }


    int i=0;
    int j=0;
    int k=0;
    int out[500]={0};
    while(i<len1&&j<len2) {
        out[k++] = arr1[i] < arr2[j] ? arr1[i++] : arr2[j++];
    }//所有重复的都进入了out
    while (i<len1){
        out[k++]=arr1[i++];
    }//arr1剩下的也有重复的
    while(j<len2){
        out[k++]=arr2[j++];
    }

    //去重输出
    int idx=1;
    int ans[500];//存放不重复元素的数组
    ans[0] = out[0];
    for(int i=1;i<500;i++){
        if(out[i] != out[i-1]){
            ans[idx++] = out[i];
        }
    }
    idx--;

    for(int i=0; i < idx; i++){
        printf("%d ", ans[i]);
    }

}
