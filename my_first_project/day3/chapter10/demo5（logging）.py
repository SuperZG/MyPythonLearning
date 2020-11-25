import logging
logging.basicConfig(level=logging.INFO)
# 而是通过修改异常显示的级别,来帮助我们确认异常的原因

def division(num):
    divided = int(num)
    logging.info('The divided is 0!', divided)
    return 10 / divided


division(0)
