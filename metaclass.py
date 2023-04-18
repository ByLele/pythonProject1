#metaclas M是A的元类

class M(type):
    def __new__(cls,name,bases,dict):
        print(name,bases,dict)
        return type.__new__(cls,name,bases,dict)
#TODO:用法1规范类的建立 1.不允许建立一些类
    def __new__(cls,name,bases,dict):
        print(name,bases,dict):

    def __init__(self,name,bases,dict):
        #运行init时已经有 A object
        print(name,bases,dict)
        return type.__init__(self,name,bases,dict)

    def __call__(self,*args,**kwargs):#TODO:call ()时调用  注意 cls self
        print("call")
        return type.__call__(cls,*args,**kwargs)
        #return supper.__call__(cls,*args,**kwargs)
class A(metaclass=M):#等价于A = M("A",(),{})
    pass

#type建立class     TODO:type.__new__(cls,name,bases,dict)
A = type("A",(),{})

A = M("A",(),{})