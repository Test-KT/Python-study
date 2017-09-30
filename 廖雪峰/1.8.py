# -*- coding: utf-8 -*-
#　高阶特性


def old():
    yield 'one'
    yield 'two'
    yield 'three'
    yield 'four'

if __name__ == '__main__':
    ''' 切片操作 '''
    citys=['gz','sz','sh','bj']
    print(citys[0:1])  #取从０开始的１个参数,后面的1代表取多少个
    print(citys[-1:-2]) #可以倒过来取
    print(citys[-2:])
    print(citys[:2]) #从0开始取3个参数,如果是０可以忽略
    print(citys[::2]) #2代表每个２取一个参数
    L=list(range(100))
    print(L[::5])

    print('abcdefg'[::3])

    ''' 列表生成器 '''
    print([x*x for x in range(1,11)])
    
    print([x*x for x in range(1,11) if x%2==0])

    print([m+n for m in 'ABC' for n in 'DEF'])

    import os
    print([d for d in os.listdir('../')])


    L=['A','b','c']
    print([s.lower() for s in L])


    import collections

    L = ['Hello', 'World', 18, 'Apple', None]
    print([s.lower() for s in L if isinstance(s,str)])


    ''' 生成器 '''
    g=(x*x for x in range(1,5))
    print(g)
    print(next(g))
    for i in g:
        print(i)


    for i in old():
        print(i)
    from collections import Iterable
    print(isinstance(old(),Iterable))
    


    