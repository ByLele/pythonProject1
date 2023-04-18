"""
class里定义的函数是怎么变成方法的？函数里的self有什么特殊意义么？
定义class 命名空间运行code block ，code block 内 local variable变成class内的__dict__

"""
class A:
    def f(self,data):#产生了一个function object
        print(self.name)
        print(data)

o = A()
o.name = "Bob"
#print(A.f)#<function A.f at 0x1008a87c0>
#print(o.f)#<bound method A.f of <__main__.A object at 0x1009d6210>>
#myfunc = o.f  #descrption 描述器
#myfunc("hello")

A.f(o,"hello")
o.f("hello")

A.f = f
o = A()
o.f("hello")