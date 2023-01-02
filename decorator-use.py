import time

def log_function(func):
    def wrappers(*args,**kwargs):
        print(f"function start!")
        print(f"args:{args}")
        ret= func(*args,**kwargs)
        print(f"function end!")
        return ret
    return wrappers


@log_function
def fib(n):
    if n <= 1:
        return 0
    return fib(n-1)+fib(n-2)

fib(4)

def log_func(level = "trace"):
    def inner(func):
        def wrappers(*args,**kwargs):
            print(f"function args:{args}!")
            ret = func(*args,**kwargs)
            print(f"function end!")
            return ret
        return wrappers
    return inner
