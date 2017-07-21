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

