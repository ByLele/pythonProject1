#metaclas M是A的元类

class M(type):
    def __new__(cls,name,bases,dict):
        print(name,bases,dict)
        return type.__new__(cls,name,bases,dict)


class A(metaclass=M):#等价于A = M("A",(),{})
    pass

#type建立class
A = type("A",(),{})

A = M("A",(),{})