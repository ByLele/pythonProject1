import dis

#TODO:code object
def f(a):
    import math
    a.attr
    b=a.method()
    return b
code=f.__code__
dis.dis(f)
print(f"nlocals:{code.co_nlocals}")
print(f"VarnameS：{code.co_varnames}")
print(f"nameS：{code.co_names}")
print(f"cellvars:{code.co_cellvars}")
print(f"freevars:{code.co_freevars}")
print(f"consts:{code.co_consts}")

#if __name__ == "__main__":