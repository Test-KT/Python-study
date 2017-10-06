# -*- coding: utf-8 -*-
#　类和实例/访问权限/继承多态／实例属性/类属性

class Student(object):
    UID=0x11111111
    __xid=10
    def __init__(self,name,city):
        self.__name=name
        self.__city=city
    def toString(self):
        print('[name:%s,city:%s]'%(self.__name,self.__city))

    def getName(self):
        return self.__name
    def getCity(self):
        return self.__city
    def __len__(self):
        return 100

class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    pass
class Cat(Animal):
    pass

 
if __name__ == '__main__':
    s=Student('lsl','gz')
    print(s.getName(),s.getCity())
    s.toString()
    a=Animal()
    d=Dog()
    c=Cat()
    
    d.run()
    c.run()
    

    print(isinstance(d,Animal))
    print(isinstance(d,Cat))
    print(isinstance(a,Dog))
    print(len(s))
    print(dir(s))
    
    if hasattr(d,'run'):
        print('you')
    else:
        print('not you')

    print(s.UID)
    s.UID=111
    print(s.UID)
    del s.UID
    print(s.UID)

   