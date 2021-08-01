'''
1．按要求编写程序
接收键盘输入的m和n的值，要求判断m与n为正整数并且m<n，否则继续输入，
寻找m到n之间的所有正整数的反序数中的素数，将结果写到输出文件“out.txt”中。
反序数：将原数各位数字颠倒后的数，例如：123的反序数为321，70的反序数为7。
本题要提交程序12_1.py与结果文件out.txt共两个文件。

'''
while 1:
    m=int(input('enter m: '))
    n=int(input('enter n: '))
    if m>0 and n>0 and m<n:
        break
    else:
        print('m与n为正整数并且m<n,请重新输入')


def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True


def fanxu(num1:int,num2:int)->list:
    out=[]
    if num1>num2:
        num1,num2=num2,num1
    for n in range(num1,num2+1):
        if is_prime(int(str(n)[::-1])):
            out.append(n)
    return out


def save_out(out:list,filepath):
    with open(filepath,'w') as f:
        for n in out:
            f.write(str(n)+'\n')


save_out(fanxu(n,m),'out.txt')
