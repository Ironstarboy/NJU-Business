'''
读出文件“file1.txt”中的字符串，采用行程长度压缩编码方法RLC进行压缩，并将结果写入“file2.txt”中。
测试数据：
“file1.txt”中的字符串：aaaaabbbbcccddddaafff
运行结果：
“file2.txt”中的字符串：a5b4c3d4a2f3
file1.txt文件使用如上格式自行建立，例如windows中用记事本创建，并存放在程序同一个文件夹下。
最后提交程序文件12_3.py与file1.txt、file2.txt文件共三个文件。

'''

def RLC(s):
    letters=list(map(lambda x:chr(x),range(ord('a'),ord('z'))))
    num=[]
    for l in letters:
        num.append(s.count(l))

    out=''
    for i in range(len(num)):
        if num[i]>=2:
            s=letters[i]+str(num[i])
            out+=s
    return out



with open('file1.txt','r') as g:
    s=g.read()

with open('file2.txt','w') as f:
    f.write(RLC(s))
