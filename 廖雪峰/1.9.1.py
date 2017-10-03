# -*- coding: utf-8 -*-
#　＝返回函数

''' 返回函数 '''
def lazy_f():
    def hello():
        return 'hello world'
    return hello
''' 闭包 '''
def count():
    fs=[]
    for i in range(1,4):
        def d():
            return i*i
        fs.append(d)
    return fs
''' 上面函数的改良 '''
def count_():
    fs=[]
    def f(j):
        def g():
            return j*j
        return g
    for i in range(1,4):
        fs.append(f(i))
    
    return fs

if __name__ == '__main__':
    f=lazy_f()
    print(f)
    print(f())
    f1,f2,f3=count()
    print(f1(),f2(),f3())
    g1,g2,g3=count_()
    print(g1(),g2(),g3())
