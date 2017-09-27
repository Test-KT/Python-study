# -*- coding: utf-8 -*-
#　数据类型与变量

a = 'abc'  # 创建一个a内存地址存放'abc'
b = a  # 创建一个b，内存地址指向a
a = 'xyz'  # 创建一个存放'xyz'的地址，并指向a，原来的b地址指向'abc'
print(b)  # 所以b输出abc


if __name__ == '__main__':
    print('aaa')
