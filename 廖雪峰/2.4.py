# -*- coding: utf-8 -*-
#　IO读写

import os
import shutil
import time
f=open('/home/lsl/PycharmProjects/Python-study/廖雪峰/test.py','r')
print(f.read())

with open('/home/lsl/PycharmProjects/Python-study/廖雪峰/1.8.py','r') as f:
   for i in f.readline():
       print(i)

print(os.name)
print(os.path.abspath('.'))
newpath=os.path.join(os.path.abspath('.'),'new')
if os.path.exists(newpath):
    os.rmdir(newpath)
else:
    os.mkdir(newpath)
# try:
#     os.mkdir(newpath)
# except FileExistsError as e:
#     os.rmdir(newpath)

print(os.path.split('/home/lsl/PycharmProjects/Python-study/廖雪峰/1.8.py'))
print(os.path.splitext('/home/lsl/PycharmProjects/Python-study/廖雪峰/1.8.py'))
print(os.path.splitdrive('/home/lsl/PycharmProjects/Python-study/廖雪峰/1.8.py'))
print([x for x in os.listdir('.') if os.path.isdir(x)])
print([x for x in os.listdir('.') if os.path.isfile(x)])

t=os.path.getctime('/home/lsl/PycharmProjects/Python-study/廖雪峰/1.8.py')
print(time.strftime('%Y %m %d',time.gmtime(t)))


def search(file,path='.'):
    temppath=path
    for x in os.listdir(temppath):
        if os.path.isdir(x):
            search(file,os.path.join(temppath, x))
        else:
            if x.find(file)!=-1:
                print(x)






class OsFileAndDirs(object):
    def __init__(self,filename,time):
        self.__filename=filename
        self.__time=time
    def __repr__(self):
        return 'fileName:%s,dateTime:%s'%(self.__filename,self.__time)
def getfiletime(x):
    t=os.path.getctime(x)
    return time.strftime('%Y-%m-%d',time.gmtime(t))

def ls_l():
    L=[]
    files=os.listdir('.')
    for x in files:
        temp=OsFileAndDirs(x,getfiletime(x))
        L.append(temp)
    return L
if __name__ == '__main__':
    print(list(ls_l()))

    search('2')




    