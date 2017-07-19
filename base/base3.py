# 字典学习  字典类似java 中的map集合
"""
    list比较，dict有以下几个特点：
    查找和插入的速度极快，不会随着key的增加而变慢；
    需要占用大量的内存，内存浪费多。
    而list相反：
    查找和插入的时间随着元素的增加而增加；
    占用空间小，浪费内存很少。
"""
d={'lsl':24,'gy':25}
print(d)

print(d['lsl'])

print(d.get('gsy'))

d.pop('lsl')

d['nlt']=24

print(d)

# set 使用
s=set([1,2,3,1])
print(s)
s.add(4)


print(s)

a='abc'
b=a.replace('a','A')

print(b)
