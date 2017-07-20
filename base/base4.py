#函数

def my_abs(num):
    if num<0:
        return -num
    else:
        return num
abs(-1)
print(my_abs(0.0001))



def my_power(x,n):
    s=1;
    while n>0:
        n=n-1
        s=s*x

    return s


# print(my_power(2,10))



print(2**100000000)