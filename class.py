import dis

class A:
    name = "AAA"
    def f(self):
        print(1)


#TODO:动态建立类
#name  父类  dictionary

"""建立一个类"""
def f(self):
    print(1)

d = {
    "name":"A",
    "f":f
}

A = type("A",(),d)

if __name__ == "__main__":
    print(type(A))
    print(A.__dict__)
    AA = A
    f = A.__dict__
    dis.dis(A)