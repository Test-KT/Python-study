#迭代

# 戏称万物可迭代
for c  in 'avc':
    print(c)


for i,value in enumerate('avc'):
    print(i,value)



for x,y in [{'a':1,'b':2}]:
    print(x,y)


for i in range(1,10):
    for j in range(1,i+1):
        print('{}*{}={}\t'.format(i,j,i*j),end='')
    print()


for i in (x*x for x in range(1,10)):
    print(i)

# 杨辉三角，好难懂你额
def _yh(max):
    L=[1]
    m=1
    yield L
    while m<max:
        G=[]
        n=0
        while n<=m:
            if n==0:
                G.insert(n,L[n])
            elif n==m:
                G.insert(n,L[-1])
            else:
                G.insert(n,L[n-1]+L[n])
            n=n+1
        yield G
        L=G
        m=m+1

for i in _yh(5):
    print(i)




                