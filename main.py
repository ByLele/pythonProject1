# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。

import time
import schedule

def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。

def job_that_exechtes_once():
    print('Hello')
    #return schedule.CancelJob


schedule.every().day.at('00:24').do(job_that_exechtes_once)


while True:
    schedule.run_pending()
    time.sleep(1)

print_hi('PyCharm')

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
def log(level="debug"):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s call %s' % (level, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log()
def func_b(name):
    print("this is a test. name:%s" % name)


def a_new_decorator(a_func):
    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")

        a_func()

        print("I am doing some boring work after executing a_func()")

    return wrapTheFunction






if __name__ == '__main__':
    @a_new_decorator
    def a_function_requiring_decoration():
        """Hey you! Decorate me!"""
        print("I am the function which needs some decoration to "
              "remove my foul smell")


    a_function_requiring_decoration()
    # outputs: I am doing some boring work before executing a_func()
    #         I am the function which needs some decoration to remove my foul smell
    #         I am doing some boring work after executing a_func()

    # the @a_new_decorator is just a short way of saying:
    a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
    print(a_function_requiring_decoration.__name__)
