# -*- coding: utf-8 -*-
''' 函数 '''

def power(x,n=2):
    s=1
    while n>0:
        n-=1
        s=s*x
    return s
def add_end(L=None):
    if L is None:
        L=[]
    L.append('END')
    return L

def calc(nums):
    if isinstance(nums,(list,tuple)):
        sum=0
        for s in nums:
            sum=sum+s*s
        return sum
    else:
        return '参数不对'

def calc_(*nums):
    sum=0
    for n in nums:
        sum=sum+n*n
    return sum
''' 递归函数 '''
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
def add_fact(n):
    if n==1:
        return 1
    return n+add_fact(n-1)

''' 尾递归优化 '''
def add_fact_(n):
    return add_fact_iter(n,1)
def add_fact_iter(n,p):
    if n==1:
        return p
    return add_fact_iter(n-1,n+p)

def fact_(n):
    return fact_iter(n,1)
def fact_iter(n,p):
    if n==1:
        return p
    return fact_iter(n-1,n*p)
if __name__ == '__main__':
    print(power(2))
    print(power(2,10))
    print(add_end([1,2,3]))
    print(add_end([1,2,3]))
    print(add_end([1,2,3]))

    print(calc([1,2,3]))
    print(calc_(1,2))


    print(fact(4))

    print(add_fact(100))

    print(fact_(4))


    print(add_fact_(100))
