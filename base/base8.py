# -*- coding: utf-8 -*-

def main():
    print('lsl')
def sum(x,y):
    return x+y




if __name__ == '__main__':
    main()
    try:
        print('输入数字：')
        x=input()
        print('再次输入数字:')
        y=input()
        print(sum(int(x),int(y)))
    except ValueError:
        print('参数不是整数')

    lists=['list']
    lists.insert(0,'lsl')
    lists.sort()
    
    
    