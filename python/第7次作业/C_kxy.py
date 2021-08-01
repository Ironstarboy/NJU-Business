# x=input()
x='i am a student.'
a=list(map(chr,range(ord('a'),ord('z')+1)))
alist=[]
aInfo={}.fromkeys(a,0)
for m in x:
        if m.isalpha():
                m=m.lower()
                aInfo[m]+=1
alist.extend(aInfo.values())
print(alist)
