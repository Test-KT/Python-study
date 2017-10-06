# -*- coding: utf-8 -*-
#　日志断点测试

import logging
logging.basicConfig(level=logging.DEBUG)

def foo(s):
    n=int(s)
    # assert n!=0,'n is zero'
    logging.info('n=%d'%n)
    logging.debug('debug信息')
    return 10/n

if __name__ == '__main__':
    print(foo('１'))
    