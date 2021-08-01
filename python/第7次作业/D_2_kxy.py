nums=eval(input())

total_prime_factors=[]  # 存入4个数的所有素因子
for i in nums:
    if int(i**0.5)**2==i:  # 筛选出平方数i
        prime_factors = [] #存i的素因子
        for j in range(2, int(i ** 0.5) + 1):  # j遍历比平方数i小的数字
            if i % j == 0 :# 判断j是不是平方数的因子
                # 下面在判断j是不是素数
                prime_flag=1 # 是否为素数的标志，1代表是，0不是
                for k in range(2,int(j**0.5)+1):
                    if j%k==0:
                        prime_flag=0
                if(prime_flag):
                    prime_factors.append(j) # 列表存入当前平方数的素因子
        total_prime_factors.extend(prime_factors)

print(','.join(map(str,sorted(total_prime_factors))))






