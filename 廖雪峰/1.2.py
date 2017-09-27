# -*- coding: utf-8 -*-
#　list和tuple


if __name__ == '__main__':
    classs=['apple','bannam','pen']
    print(classs)
    classs.pop()
    print(classs)
    classs.insert(1,'gz')
    print(classs)
    classs.insert(4,'lsl') # 超出列表长度插入居然没有出现异常....
    print(len(classs))
    # classs.remove(5) 会抛出异常
    classs=[]
    print(classs)


    tuples=('lsl')  #创建后会不可变
    
    tuples=('lsl','lsl')
    print(tuples)
    