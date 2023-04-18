def gen(num):
    while num > 0:
        yield num #yield sheng c
        num -= 1
    return

g = gen(5)#返回生成器对象
#生成器状态保存到frame

first = next(g)
print(f"first:{first}")

print(f"send: {first.send(10)}") #send改变generator 状态
for i in g: # 不停next 
    print(i)

import dis
#dis.dis(g)

#生成器send
