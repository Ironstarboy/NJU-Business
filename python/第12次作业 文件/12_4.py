'''
编写程序，输入若干个字符串，判断其是否符合Python标识符命名规则，
若符合则写入到name.txt文件中，
不符合则输出不符合信息，字符串输入以“END”截止。将name.txt文件中的内容输出。
测试数据(间隔符随意些，不限制)：
a%1,   _a12,   aaa,   $ss,   1sss,   END
本题要提交程序12_4.py与结果文件name.txt共两个文件。

'''

test_data='a%1,   _a12,   aaa,   $ss,   1sss,   END'
with open('name.txt','w') as f:
    my_name=test_data.replace(' ','').split(',')
    for i in my_name:
        if i!='END':
            if i.isidentifier():
                f.write(i+'\n')
        else:
            break


