# -*- coding: utf-8 -*-
#　枚举类/元类


from enum import Enum,unique
import test

@unique  #保证没有重复值
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

if __name__ == '__main__':
    Moth=Enum('Moth',('Jan','Feb'))

    for name,m in Moth.__members__.items():
        print(name,m,m.value)

    day1=Weekday.Mon
    print(day1)
    print(Weekday['Mon'].value)
    
    test.syo('a','b')

