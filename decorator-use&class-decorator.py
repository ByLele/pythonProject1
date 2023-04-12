import time
import dis 
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

# def log_func(level = "trace"):
#     def inner(func):
#         def wrappers(*args,**kwargs):
#             print(f"function args:{args}!")
#             ret = func(*args,**kwargs)
#             print(f"function end!")
#             return ret
#         return wrappers
#     return inner
# class Decorators:
#     def log_function(self,func):
#         def wrapper(*args,**kwargs):
#             print("function start!")
#             print(f"args:{args}")
#             ret = func(*args,**kwargs)
#             print("func end!")
#             return ret
#         return wrapper

# @Decorators.log_function
# def fib(n)
#     if n <= 1:
#         return 0
#     return fib(n-1) + fib(n-2)
# def log_func(level="trace"):
#     def inner(func):
#         def wrapper(*args, **kwargs):
#             print(f"function start! level:{level}")
#             print(f"args:{args}")
#             ret = func(*args, **kwargs)
#             print("function end!")
#             return ret
#         return wrapper
#     return inner

class Decorators:
    @staticmethod
    def log_function(func):
        def wrapper(*args, **kwargs):
            print("function start!")
            print(f"args:{args}")
            ret = func(*args, **kwargs)
            print("function end!")
            return ret
        return wrapper

    @log_function
    def fib(n):
        if n <= 1:
            return 0
        return fib(n-1) + fib(n-2)

f = fib(5)
print(f)
dis.dis(fib)
