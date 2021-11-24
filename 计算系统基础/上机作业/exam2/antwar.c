#include <stdio.h>
struct warplace{
    //战场，可以容纳2个蚂蚁
    int up;
    int down;
};
int can_move(struct warplace* s, int pos, int n){
    //判断是否当前蚂蚁是否能继续移动
    int flag=0;
    if(pos<n-1){
        for(int i=pos+1;i<n;++i){
            if(s[i].up <= 0){
                flag=1;
                break;
            }
        }
    }
    return flag;
}
void move(struct warplace* s,int n ){
    //所有蚂蚁移动一步,可以认为负数蚂蚁不动，只有正蚂蚁移动。都动会交叉错位
    //n是蚂蚁数量
    for(int i=0;i<n;++i){
        if(can_move(s, i,n)){
            if(s[i].up > 0){
                s[i+1].down=s[i].up;//移动到新位置
                s[i].up=0;//原位置清零
            }
        }
    }
}
void war(struct warplace*s,int n){
    //开始交战，死亡的蚂蚁记录为0,并更新 up b数据和次序
    for(int i=0;i<n;++i){
        int abs_a= s[i].up > 0 ? s[i].up : -1 * s[i].up;
        int abs_b= s[i].down > 0 ? s[i].down : -1 * s[i].down;
        if(abs_a>abs_b){
            s[i].down=0;
        }
        if(abs_a==abs_b){
            s[i].up=0;
            s[i].down=0;
        }
        if(abs_a<abs_b){
            s[i].up=s[i].down;
            s[i].down=0;
        }
    }
}

int main(){
    int n;//蚂蚁数量
    scanf("%d",&n);
    int count=0;
    struct warplace antsplace[10000];
    while (count<n){
        antsplace[count].down=0;
        scanf("%d",&antsplace[count++].up);
    }
    int time=0;
    while(time++<n){
        move(antsplace,n);
        war(antsplace,n);
    }

    for(int i=0;i<n;i++){
        if(antsplace[i].up != 0){
            printf("%d ",antsplace[i].up);
        }
    }
}