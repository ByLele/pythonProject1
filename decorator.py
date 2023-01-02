import os
import time
import dis
from mylog import CLog

from functools import wraps
cur_path = os.path.abspath(os.path.dirname(__file__))
project_name = "pythonProject1"
root_path = cur_path[:cur_path.find(project_name)]
log_path = root_path + "\log"
# logger = CLog(log_path)
logger = CLog(log_path)
#简单装饰器
# def decorator_a(fn):
#     fn()
#     logger.info("in decorator_a")
#     localtime = time.asctime(time.gmtime(time.time()))
#     print(localtime, "is decorator_a fn")
#
#
# @decorator_a
# def decorator_b():
#     localtime = time.asctime(time.gmtime(time.time()))
#     print(localtime, "is docorator_b")
#

#TODO：带参数装饰器
def decorator_log(level="debug"):
    def decorator(func): #函数
        #@wraps(func)
        def wrapper(*args,**kwargs):#参数
            logger.info(f"带参数装饰器: locals= {locals()}")
            #print(locals())
            print("%s call %s"% (level,func.__name__))
            return func(*args,**kwargs)
        return wrapper
    return decorator
@decorator_log()
def decorator_log_a(name):
    print('this is test name:%s' %name)

#TODO:class相关装饰器  @property会将类方法当作属性来使用
class car:
    def __init__(self,name,price):
        self._name = name
        self._price = price
    @property
    def car_name(self):
        return self._name
#  class相关
class static_car:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    @property
    def car_name(self):
        return [self.name,self.price]

    @staticmethod
    def print_all_carname():
        print("all car name.[bc,bm,lh,bz]")
    @classmethod
    def get_car_name(cls):
        print("class_method car name: %s" % cls("bm",129).car_name)
    #TODO:staticmethod与classmethod方法异同
    """
    @staticmethod,不用对象自身self对象cls参数，使用类特定类名.方法
    @classmethod, 有cls参数，可以调用类的属性，类的方法，实例化对象
    """
#TODO：类作为装饰器
class Foo:
    def __init__(self,func):
        self._func = func
    def __call__(self,*arg,**kw):
        print("__call__func__name:%s" % self._func.__name__)
        self._func(*arg,**kw)

@Foo
def print_msg(code,message):
    print("code:%d msg:%s" %(code,message))

#TODO：带参数装饰器原理
def timeit(iteration):
    def inner(f):
        def wrapper(*args,**kwargs):
            start = time.time()
            for _ in range(iteration):
                ret = f(*args,**kwargs)
            print(time.time()-start)
            return ret
        return wrapper
    return inner
@timeit(1000)
def double(x):
    return x*2


#TODO:类的装饰器  输入类返回类
def add_print(cls):
    def __str__(self):
        return str(self.__dict__)
    cls.__str__ = __str__
    return cls
@add_print
class MyObject:
    def __init__(self,a,b):
        self.a = a
        self.b = b
if __name__ == "__main__":
    #等价于  MyObject = add_print(MyObject)
    o = MyObject(1,2)
    print(o)
    #decorator_b  #简单装饰器
    #decorator_log_a("good")
    #a_car = car("bwm",123)
    #print("car name %s" % a_car.car_name)
    #static_car.get_car_name()
    #print_msg(200,"success")
    #dis.dis(print_msg)
    #double(2)

    # inner = timeit(1000)
    # double = inner(double)
    pass