// 给定两个数组，编写⼀个函数来计算它们的交集。
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_LEN 100000

char input1[MAX_LEN];
char input2[MAX_LEN];
int array1[MAX_LEN / 2];
int array2[MAX_LEN / 2];
int already_out[MAX_LEN / 2];
int already_out_pointer = 0;
int array1_len = 0;
int array2_len = 0;


int main() {

    // 这题的输入一点格式都没有, 想不到怎么优雅地输入...
    scanf("%[^\n]%*[\n]", input1);
    scanf("%[^\n]", input2);
    char* temp;

    const char delim[2] = " ";
    temp = strtok(input1, delim);
    while (temp != NULL) {
        array1[array1_len++] = atoi(temp);
        temp = strtok(NULL, delim);
    }

    scanf("%[^\n]", input2);
    temp = strtok(input2, delim);
    while (temp != NULL) {
        array2[array2_len++] = atoi(temp);
        temp = strtok(NULL, delim);
    }
    // 终于输入完了...



    // 数据大一点肯定直接 TLE 了.(
    // 先写原来的方法. 等下写个优化方法.
    for (int i = 0; i < array2_len; i ++) {
        for (int j = 0; j < array1_len; j ++) {
            if (array2[i] == array1[j]) {

                int print_flag = 1;

                for(int k = 0; k < already_out_pointer; k ++) {
                    if (already_out[k] == array2[i]) {
                        print_flag = 0;
                        break;
                    }
                }

                if (print_flag) {
                    printf("%d ", array2[i]);
                    already_out[already_out_pointer++] = array2[i];
                }
                break;
            }
        }
    }

    return 0;
}
