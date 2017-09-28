# -*- coding: utf-8 -*-
''' 定义函数 '''

import math
def my_max(a,b):
    if not isinstance(a,(int,float)):
        raise TypeError('类型错误')
    if not isinstance(b,(int,float)):
        raise TypeError('类型错误')
    if a>b:
        return a
    else:
        return b


def my_return(x,y,z=10):
    return x,y,z


def my_fc(a,b,c):
    z=b*b-4*a*c
    print(z)
    if z>=0:
        x1=(-b+math.sqrt(z))/(2*a)
        x2=(-b-math.sqrt(z))/(2*a)
        return x1,x2
    else:
        return '无解'
        
if __name__ == '__main__':
    m=my_max(1,2)
    print(m)

    # my_max('lsl',11)

    print(my_return(1,2))
    print(math.pi)

    print(my_fc(5,4,0))


