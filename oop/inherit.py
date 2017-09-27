# import types  #判断类型是否是函数
class Animal(object):
    def run(self):
        print('Animal is runing...')




class Dog(Animal):
    def run(self):
        print('dog is runing ')

class Cat(Animal):
    def run(self):
        print('cat is runing ')






if(__name__=='__main__'):
    dog=Dog()
    dog.run()
    cat =Cat()
    cat.run()
    print(isinstance(dog, Animal))

    print(isinstance(cat,Dog))


    def test_run(animal):
        animal.run()

    
    test_run(Dog())


    print(type(dog))


    print(type(test_run))

    print(dir(dog))
