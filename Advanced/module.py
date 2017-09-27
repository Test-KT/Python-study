#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__autor__='lsl'
import  sys
def test():
    args=sys.argv
    if len(args)==1:
        print('Hello world!')
    elif len(args)==2:
        print('Hello %s'%args[1])
    else:
        print('too many')

if __name__=='__main__':
    print(__autor__)
    
    
    t=test()
    print(__name__)
  