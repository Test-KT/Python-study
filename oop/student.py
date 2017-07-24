class Student(object):
    """
        变量加上两个_变为私有变量 ,其实加上双下划线之后,原来的__city 变为  _Student_city,通过这个，还是可以访问的
    """
    def __init__(self,name,city):
        self.name=name   
        self.__city=city
        
    def getName(self):
        return self.name
    def getCity(self):
        return self.__city
    def setName(self,name):
        self.name=name
    def setCity(self,city):
        self.__city=city


if(__name__=='__main__'):
    s=Student('lsl','gz')
    print(s)
    s.like='nlt'
    print(s.setName('GY'))
    print(s.getName())
    print(s._Student__city) 
    