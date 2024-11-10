import asyncio

async def main():
    print("hello")
    await asyncio.sleep(1)
    print("world")






coro = main()
asyncio.run(coro)

"""
couroutines 调用

"""


async def main_task():
    await asyncio.create_task(
    asyncio.sleep(1)
    )

asyncio.run(main_task())



# coroutine 和 tash 区别

# event loop 最小调度单位 task   

# await 后内容可以是一个   coroutine 也可以是一个 task ,可以是一个future



