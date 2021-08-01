'''
创建一个文件Blowing in the wind.txt，
⑴在文件头部插入歌名“Blowin'in the wind”
⑵在歌名后插入歌手名“Bob Dylan”
⑶在文件末尾加上字符串“ 1962 by Warner Bros. Inc.”
⑷在屏幕上打印文件内容
文件Blowing in the wind.txt使用如上格式自行建立，例如windows中用记事本创建，并存放在程序同一个文件夹下。
最后提交程序文件12_6.py与处理后的文件共2个文件。
'''
with open('Blowing in the wind.txt','w') as f:
    f.write('''How many roads must a man walk down
Before they call him a man
How many seas must a white dove sail
Before she sleeps in the sand
How many times must the cannon balls fly
Before they're forever banned
The answer my friend is blowing in the wind
The answer is blowing in the wind''')

# r+,w+,w有覆写问题
with open('Blowing in the wind.txt','r+') as f:
    # ⑴在文件头部插入歌名“Blowin'in the wind”
    # ⑵在歌名后插入歌手名“Bob Dylan”
    old_text=f.read()
    new_text="Blowin'in the wind"+'\n'+'Bob Dylan'+'\n'+old_text

    f.seek(0,0)
    f.write(new_text)

    # ⑶在文件末尾加上字符串“ 1962 by Warner Bros. Inc.”
    f.seek(0,2)
    f.write('1962 by Warner Bros. Inc.')

    # ⑷在屏幕上打印文件内容
    f.seek(0,0)
    print(f.read())


