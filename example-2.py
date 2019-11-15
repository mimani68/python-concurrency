import asyncio
# 
# python 3.4
# 
# Borrowed from http://curio.readthedocs.org/en/latest/tutorial.html.
# https://snarky.ca/how-the-heck-does-async-await-work-in-python-3-5/
# 
# --------------------------------------------
#  
#    python 2
#   ----------------
#  $ python simple-yield-asyncio.py
# 
#    File "simple-yield-asyncio.py", line 13
#    yield from asyncio.sleep(1)
#             ^
#    SyntaxError: invalid syntax
# 
@asyncio.coroutine
def countdown(id, n):
    while n > 0:
        print('Task({}) in {} time'.format(id, n))
        yield from asyncio.sleep(0)
        n -= 1

@asyncio.coroutine
async def countdownAsync(id, n):
    while n > 0:
        print('Task({}) in {} time'.format(id, n))
        await asyncio.sleep(0)
        n -= 1

loop = asyncio.get_event_loop()

tasks_with_asyncio = [
    asyncio.ensure_future(countdown("A", 5)),
    asyncio.ensure_future(countdown("B", 3))
]

tasks= [
    countdownAsync("A", 5),
    countdownAsync("B", 3)
]

# 
# 
# 
asyncio.wait(tasks)
loop.run_forever()

# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()
