import logging

def Diomod(x,y):
    try:
        if not(isinstance(x,(int,float)) and isinstance(y,(int,float))):
            logging.debug('被除数或除数的类型不对！')
            raise TypeError('被除数或除数的类型不对！')
        if y==0:
            logging.info('除数不能为0！')
            raise ValueError('除数不能为0！')
    except Exception as E:
        print('输入错误：',E)
    else:
        print('输入正确，结果为：',x/y)
if __name__ == '__main__':
    logging.basicConfig(filename=r'D:\Python\Log.log', filemode='a', level=logging.DEBUG,
                        datefmt='%Y-%m-%d %H:%M:%S', format="%(asctime)s %(filename)s"
                                                            "[line:%(lineno)d]%(levelname)s-%(message)s")
    Diomod(10,0)
    Diomod('a',1)
    Diomod(10,2)
    logging.warning('warning message!')
    logging.error('error message!')
    logging.critical('critical message!')