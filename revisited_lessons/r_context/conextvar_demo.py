from __future__ import annotations

from contextvars import ContextVar

var: ContextVar[int | str] = ContextVar('var', default="var")


def set_var_in_same_task():
    token1 = var.set("this is value")
    token2 = var.set("this is another value")
    return token1, token2


async def coro():
    var.set('value in coro')
    print(var.get())


async def main():
    var.set('value in main')
    print(var.get())
    await coro()  ## switch
    print(var.get())


if __name__ == '__main__':
    t1, t2 = set_var_in_same_task()
    print(var.get())
    var.reset(t2)
    print(var.get())
    var.set(123)
    print(var.get())
    var.reset(t1)
    print(var.get())

    print("run asyncio")
    import asyncio

    asyncio.run(main())
