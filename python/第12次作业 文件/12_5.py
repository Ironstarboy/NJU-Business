'''
字幕文件subtitles.srt如下：编写程序取字幕文件其中的文本写入到新建的文件中。


字幕文件subtitles.srt使用如上格式自行建立，例如windows中用记事本创建，并存放在程序同一个文件夹下。
最后提交程序文件12_5.py与结果文件titles.txt共2个文件。
'''

with open('subtitles.srt','r',encoding='utf-8') as f:
    lines=f.readlines()
    text=list(filter(lambda x:lines.index(x)%4==2,lines))

with open('titles.txt','w',encoding='gbk') as f:
    for i in text:
        f.write(i)