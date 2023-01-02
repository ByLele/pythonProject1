"""mro 所有继承类排队"""

class A:
    def say(self):
        print('A')

class B(A):
    def say(self):
        print('B')

class C(A):
    pass


class M(C,B):
    pass


m = M()

m.say()
print(M.mro())  #查看class继承顺序
"""
c3算法
local precedence code 局部优先
monopriority 单调性

"""