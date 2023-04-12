import dis
#类的背后是什么
class A:
    name = "AAA"
    def f(self):
        print(1)


#TODO:动态建立类
#name  父类  dictionary
#TODO:这就是类
"""建立一个类"""
def f(self):
    print(1)

d = {
    "name":"AAA",
    "f":f
}

A = type("AAA",(),d)

if __name__ == "__main__":
    print(type(A))
    print(A.__name__)
    print(A.__dict__)
    AA = A
    f = A.__dict__
    dis.dis(A)