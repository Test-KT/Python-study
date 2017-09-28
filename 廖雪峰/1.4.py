# -*- coding: utf-8 -*-
''' 循环 '''

lists=['lsl','gz','th']

for i in lists:
    print(i)
sum=0
for i in range(1,4):
    sum+=i
print(sum)


print(tuple(range(0,11,2)))
sum=0
for i in range(0,100):
    sum=sum+i+1
print(sum)

for i in 'lishoulin':
    print(i)

sum=0;
n=99
while n>0:
    sum+=n
    n-=2
print(sum)