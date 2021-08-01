
pyin=input().split(',')
# 'Kim is a bookkeeper, Kate is an actress, Bartholomew is a barber.'

names=[]
careers=[]
def get_name(s):
    s=s.strip()
    space_index=s.index(' ')
    name=s[:space_index]
    return name

def get_carrer(s):
    s=s.strip()
    space_index=s.rindex(' ')
    carrer=s[space_index+1:].strip('.')
    return carrer
for s in pyin:
    names.append(get_name(s))
    careers.append(get_carrer(s))

dic=dict(zip(names,careers))
print(sorted(dic.items()))
print(sorted(dic.items(),key=lambda x:len(x[1]))[-1])