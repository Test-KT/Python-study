# -*- coding: utf-8 -*-
#　高阶函数 map/reduce
from functools import reduce

def add(x,y,f):
    return f(x)+f(y)

def f(x):
    return x+1

def fx(x):
    return x*x

def pstr(x):
    return str(fx(x)) 

def add_ad(x,y):
    return x+y


def fn(x,y):
    return x*10+y

def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}.get(s)


def paseName(x):
    return x.title()

def pase2up(s):
    return s[0].upper()+s[1:]
    
if __name__ == '__main__':
    print(add(1,2,f))
    print(add(-1,-2,abs))


    print(list(map(fx,[1,2,3,4,5,6])))

    print(list(map(pstr,[1,2,3,4,5,6])))

    r=reduce(add_ad, [1,2,3])
    print(r)

    print(reduce(fn,[1,2,3,4]))

    print(list(map(char2num,'1234s5a')))

    print(reduce(fn,map(char2num,'12345')))

    print('avc'.title())


    print(list(map(paseName,['lsl','gz','sz'])))


    print(list(map(pase2up,['lsl','gzZ','sz'])))