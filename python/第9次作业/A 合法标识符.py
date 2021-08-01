'''
字符串有一个 isidentifier ()方法，功能是用来判断给定的字符串是否为合法的标识符（
首字符为字母或下划线，其他字符为字母、下划线或数字），
请自行实现此方法的相似功能， 定义一个函数 CheckId()，
主模块中接收参数 s， 判断 s 是否为合法标识符， 输出判断结果的信息：
（1）合法： 输出'Valid identifier.';
（2）首字母不合法： 输出'Error. First char must be alphas or _.';
（3）首字母合法其他字符不合法： 输出'Error. Other chars must be alphas number or _.'。
输入
输入一个字符串。
输出
输出判断结果信息。

样例输入
_valid_identifier
样例输出
Valid identifier.
提示
一定要注意输出的字符串，不能多也不能少，例如“Error.”后有一个空格。

主模块中的语句：

CheckId(input())
'''

def check_letter_(letter):
    '''
    判断单个字符是否是字母或者下划线
    :param letter:
    :return:
    '''
    lower_letters=list(map(lambda x:chr(x),range(ord('a'),ord('z'))))
    upper_letter=list(map(lambda x:chr(x),range(ord('A'),ord('Z'))))
    if letter in lower_letters or letter in upper_letter or letter=='_':
        return True
    return False


def check_number(letter):
    '''
    检查单个字符串是否为数字
    :param letter:
    :return:
    '''
    if ord('0')<=ord(letter)<=ord('9'):
        return 1
    return 0

def CheckId(s):

    first_letter=s[0]
    other_letter=s[1:]
    isvalid_first=0
    isvalid_others=1

    if check_letter_(first_letter):
        isvalid_first=1

    for i in other_letter:
        if ( check_letter_(i)| check_number(i) )==False:
            isvalid_others=0

    if isvalid_first and isvalid_others:
        print('Valid identifier.')
    elif not isvalid_first:
        print('Error. First char must be alphas or _.')
    elif isvalid_first and not isvalid_others:
        print('Error. Other chars must be alphas number or _.')

CheckId(input())

