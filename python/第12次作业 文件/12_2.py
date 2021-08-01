'''
通讯簿文件中存有若干个联系人的信息，每个联系人的信息由姓名和电话号码组成如下。
Zhang, 2301
Zhao 2302
Li,2304
Sun,2305
编写程序完成以下功能：输入姓名，若通讯簿文件中存在则将该联系人信息输出，若不存在则输出“Not found”。
通讯簿文件使用如上格式自行建立，例如windows中用记事本创建，并存放在程序同一个文件夹下。
最后提交程序文件12_2.py与通讯簿文件共两个文件。

'''

with open('info.txt','r') as f:
    lines=f.readlines()
    names=[]
    nums=[]
    for i in lines:
        name_num=i.replace('\n','').split(',')
        names.append(name_num[0])
        nums.append(name_num[1])
    dic=dict(zip(names,nums))

    name=input('输入姓名：')
    
    n=dic.get(name)
    if n!=None:
        print(n)
    else:
        print('Not found')