# -*- coding: utf-8 -*-
#　面向对象高级／使用__slots__／使用＠property／多重继承
from types import MethodType
import time
class People(object):
     __slots__=('age','name','fb')  #只允许age，name属性绑定到这个类里面，其他的都不能进行属性添加.方法也可以限制

def fb(self,age):
    self.age=age

class Man(object):
    @property
    def age(self):
        return int(time.strftime('%Y',time.localtime(time.time())))-self.__birth
    
    @property
    def birth(self):
        return self.__birth
    @birth.setter
    def birth(self,value):
        self.__birth=value


class Anmial(object):
    pass
class Runnable(object):
    def run(self):
        print('running...')
class Flyable(object):
    def fly(self):
        print('flying...')

class Bird(Anmial,Flyable):
    pass
class Mammal(Anmial,Runnable):
    pass

if __name__ == '__main__':
    s=People()
    s.fb=MethodType(fb,s)
    s.fb(4)
    print(s.age)

    People.fb=fb
    s1=People()
    s1.fb(5)
    print(s1.age)

    s1.name='lsl'

    # s1.core=1  被限制住不能添加属性
    # print(s1.core)

    testMan=Man()
    testMan.birth=1993
    print(testMan.birth)
    print(testMan.age)


    b=Bird()
    d=Mammal()
    b.fly()
    d.run()




    