
import functools



def end():
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            func(*args,**kw)
            print('程序结束')
            return
        return wrapper
    return decorator

@end()
def six():
    print('six six six !!')
        


six()





# 能够自定义输入日志的装饰器
def log(txt):
    def decorator(func):
        @functools.wraps(func)  #属性复制出去，如果不这样子做，后面的__name__结果会是wrapper
        def wrapper(*args,**kw):
            print('%s %s()'%(txt,func.__name__))
            # return func(*args,**kw)  #这种写法也可以哟
            func(*args,**kw)
            return
        return wrapper
    return decorator

@log('时间')
def now():
    print('2012-12-12') 


now()

print(now.__name__)