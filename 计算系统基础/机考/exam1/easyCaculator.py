class Stack():
    arr=[]
    def __init__(self):
        arr=[]

    def push(self,element):
        self.arr.insert(0,element)

    def pop(self):
        return self.arr.pop(0)

    def peek(self):
        return self.arr[0]

    def size(self):
        return len(self.arr)

import re
def in2post(exp):
    op_priority = {
            '/': 2,
            '*': 2,
            '+': 1,
            '-': 1,
            '#': 0}
    op_stack= Stack()
    out=[]
    lst = re.findall('[\+\-\*\/]|[\d]+', exp)
    op_stack.push('#')
    for i in range(len(lst)):
        op:str=lst[i]
        if op.isdigit():
            out.append(op)
        else:
            while op_priority.get(op)<=op_priority.get(str(op_stack.peek())):
                out.append(op_stack.pop())
            op_stack.push(op)

    while(op_stack.size()!=0):
        out.append(op_stack.pop())
    return out


def calc_postfix(postfix):
    """计算后缀表达式的值。"""
    stack = Stack()
    for op in postfix:
        if op.isdigit():
            stack.push(op)
        elif op=='#':
            break
        else:
            a = float(stack.pop())
            b = float(stack.pop())
            stack.push(eval("{}{}{}".format(b,op,a)))

    return stack.peek()


# s=input()
exp='3*9-6+3*7/5+53614-36254*3254'
a=calc_postfix(in2post(exp))
print(round(a))




