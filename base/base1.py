
def inputWe():
    s=input('输入你的体重!\n')
    weigth=int(s)

    if(weigth<18):
        print('过轻!')
    elif weigth<25:
        print('正常!')
    elif weigth<28:
        print('过重!')
    elif weigth<32:
        print('肥胖！')
    else:
        print('严重肥胖')





if __name__ == '__main__':
    inputWe()