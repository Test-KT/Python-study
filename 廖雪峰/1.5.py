# -*- coding: utf-8 -*-
''' 字典，类似Ｊａｖａ中的map集合 '''


dicts={'name': 'lsl','age': 24,'city': 'Gz'}    #类似java中的map
print(dicts)
for j,k in dicts.items():
    print(j,k)


sets=set([1,2,3,4,2])  #类似java中的set集合
print(sets)


s1=set([1,2,3,4])
s2=set([2,3,9])

print(s1|s2)


# set([1,2,3,(1,[2,3])])  会报错哦

