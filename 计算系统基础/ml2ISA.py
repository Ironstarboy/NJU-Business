"""
机器语言→指令集
"""
R1=''
R2 = ''
R3=''
imm16=''
ml01=''

def bin2dec(imm16):
    # 补码二进制转10进制
    num=bin(imm16).replace('0b','').rjust(16,'0')
    if num[0]=='1':
        a=int(''.join(map(lambda x:'1' if x=='0' else '0',num)),2)+1
        return -a

    return imm16

def wrapper(function):
    def f():
        print(function.__name__, end=' ')
        function()
    return f

def R():#R 类型
    print('R{} R{} R{}'.format(R1, R2, R3))

def I():
    print('R{} R{} #{}({})'.format(R1, R2, imm16,hex(imm16))) #imm16有# 10，0x两种表达

def control():#控制指令
    print('R{} #{}({})'.format(R1,imm16,hex(imm16)))

def J_type():#J 指令
    print("#{}".format(bin2dec(imm16)))

@wrapper
def ADD():
    R()

@wrapper
def ADDI():
    I()

@wrapper
def SUB():
    R()

@wrapper
def SUBI():
    I()

@wrapper
def AND():
    R()

@wrapper
def ANDI():
    I()

@wrapper
def OR():
    R()

@wrapper
def ORI():
    I()

@wrapper
def XOR():
    R()

@wrapper
def XORI():
    I()

@wrapper
def LHI():
    print('R{} {}'.format(R2,hex(imm16)))

@wrapper
def SLL():
    R()

@wrapper
def SLLI():
    I()

@wrapper
def SRL():
    R()

@wrapper
def SRLI():
    I()

@wrapper
def SRA():
    R()

@wrapper
def SRAI():
    I()

@wrapper
def SLT():
    R()

@wrapper
def SLTI():
    I()

@wrapper
def SLE():
    R()

@wrapper
def SLEI():
    I()

@wrapper
def SEQ():
    R()

@wrapper
def SEQI():
    I()

@wrapper
def LB():
    I()

@wrapper
def SB():
    I()

@wrapper
def LW():
    I()

@wrapper
def SW():
    I()


@wrapper
def BEQZ():
    print('R{} #{}'.format(R1,bin2dec(imm16)))



@wrapper
def BNEZ():
    print('R{} #{}'.format(R1,bin2dec(imm16)))

@wrapper
def J():
    J_type()

@wrapper
def JR():
    print('R{}'.format(R1))

@wrapper
def JAL():
    J_type()

@wrapper
def JALR():
    print('R{}'.format(R1))

@wrapper
def TRAP():
    J_type()

refer = {'000000': {'000001':ADD,
                    '000011': SUB,
                    '001001': AND,
                    '001010': OR,
                    '001011': XOR,
                    '001101': SLL,
                    '001110': SRL,
                    '001111': SRA,
                    '010000': SLT,
                    '010010': SLEI,
                    '010100': SEQ},
         '000001': ADDI,
         '000011': SUBI,
         '001001': ANDI,
         '001010': ORI,
         '001011': XORI,
         '001100': LHI,
         '001101': SLLI,
         '001110': SRLI,
         '001111': SRAI,
         '010000': SLTI,
         '010010': SLEI,
         '010100': SEQI,
         '010110': LB,
         '010111': SB,
         '011100': LW,
         '011101': SW,
         '101000': BEQZ,
         '101001': BNEZ,
         '101100': J,
         '011011': JR,
         '101110': JAL,
         '101111': JALR,
         '110000': TRAP}

def parse(s):
    global R1
    global R2
    global R3
    global imm16
    global ml01


    R1=int(s[-25 - 1:-21], 2)
    R2 = int(s[-20 - 1:-16], 2)
    R3=int(s[-15 - 1:-11], 2)
    imm16=int(s[-16:], 2)# python 二进制转10进制可能有坑
    ml01=s

    opcode= s[:6]
    f= s[-6:]
    if opcode=='000000':
        refer[opcode][f]()
    else:
        refer[opcode]()


if __name__=='__main__':
    # 用OCR扫描pdf题目，复制输入
    s='''00110000000000111000000000000000
00000100000000100000000000000000
00000000011000010010000000001001
10100000100000000000000000000100
00000100010000100000000000000001
00000000001000010000100000000001
10100000001000000000000000000100
10110011111111111111111111101000
11000000000000000000000000000000'''.split('\n')

    for i in s:
        parse(i.replace(' ', ''))




