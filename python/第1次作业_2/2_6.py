weight=float(input('input the weight of water:\n'))

init_temperature=0
final_temperature=0

while 1:
    init_temperature=float(input('input the initial temperature of water:\n'))
    final_temperature=float(input('input the final temperature of water:\n'))
    #液态水，最终温度》初始温度
    if(init_temperature>0 and final_temperature<100 and init_temperature<=final_temperature):
        break
    else:
        print('please input the valid number!')


Q=weight*(final_temperature-init_temperature)*4184
print("{} J energy is needed".format(Q))
