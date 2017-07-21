def calc(nums):
    sum=0
    for n in nums:
        sum=sum+n*n
    return sum


def _calc(*nums):
    sum=0
    for n in nums:
        sum=sum+n*n
    return sum



print(calc([1,2,3]))
print(_calc(1,2,3))

# print(_calc([1,2,3])) 会出现报错正确做法是
print(_calc(*[1,2,3]))


# 关键字参数

def person(**kw):
    print('other:',kw)



person(other='kkk')

list={'name':'lsl','age':24}

person(**list)


# 受限制的关键字函数

def _person(name,*,age,city):
    print('name:',name,age,city)



_person('lsl',age=24,city='gz')


# 参数有五种，可以灵活组合（必选参数、默认参数、可变参数（*arg）、命名关键字参数(**kw)、关键字参数(a,b,*,c,d)）