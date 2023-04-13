def gen(num):
    while num > 0:
        yield num
        num -= 1
    return

g = gen(5)

first = next(g)
print(f"first:{first}")

print(f"send: {first.send()}")
for i in g:
    print(i)

import dis
#dis.dis(g)

#生成器send
