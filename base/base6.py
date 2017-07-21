#递归实现阶乘
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)

# 尾递归实现阶乘
def _fact(n,1):
    return _fact_iter(n,1)

def _fact_iter(num,pro):
    if num==1:
        return 1
    return _fact_iter(num-1,num*pro)



#然而语言没有对尾递归进行优化，所以上面的都是然并卵，O(∩_∩)O哈哈哈~