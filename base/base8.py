def cale_sum(*args):
    ax=0
    for n in args:
        ax=ax+n
    return ax

print(cale_sum(1,2,3,4))


# 函数返回值
def lazy_sum(*args):
    def sum():
        ax=0
        for n in args:
            ax=ax+n
        return ax
    
    return sum



lazy=lazy_sum(1,2,3,4)
la=lazy_sum(1,2,3,4)


print(lazy==la)
print(lazy())


# 闭包一
def count():
    fs=[]
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs

f1,f2,f3=count()
print(f1())
print(f2())

# 闭包二
def _count():
    def f(i):
        def g():
            return i*i
        return g
    fs=[]
    for j in range(1,4):
        fs.append(f(j))
    return fs

g1,g2,g3=_count()

print(g1())
print(g2())
print(g3())
