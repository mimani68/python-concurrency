import asyncio
from time import sleep


# ==========================
# 
#    Library
# 
# ==========================
# @asyncio.coroutine
def doStaff():
    for i in range(5):
        sleep(1.7)
        yield from asyncio.sleep(0)
        print('[*] doStaff result: {}'.format(i+1))

# @asyncio.coroutine
async def doStaffAsync():
    for i in range(5):
        sleep(1.3)
        await asyncio.sleep(0)
        print('[*] doStaffAsync result: {}'.format(i+1))


# ==========================
# 
#    Application Layer
# 
# ==========================
# @asyncio.coroutine
async def code_with_async(label, **kwargs):
    print('[{}-top]'.format(label))
    # yield from doStaffAsync() # SyntaxError: 'yield from' inside async function
    await doStaffAsync()
    print('[{}-down]'.format(label))

# @asyncio.coroutine
def code_with_yield(label, **kwargs):
    print('[{}-top]'.format(label))
    # yield from doStaffAsync()   # TypeError: cannot 'yield from' a coroutine object in a non-coroutine generator
    # await doStaffAsync()        # Error: Undefined variable `await`
    yield from doStaff()
    print('[{}-down]'.format(label))


# ==========================
# 
#    index.py
# 
# ==========================
def main():
    # 
    # Method One
    # 
    asyncio.wait([
        asyncio.ensure_future(code_with_async('code_with_async', sleep_time=2)),
        asyncio.ensure_future(code_with_yield('code_with_yield', sleep_time=2))
    ])
    # 
    # Method Two
    # 
    # asyncio.ensure_future(code_with_async('code_with_async', sleep_time=2))
    # asyncio.ensure_future(code_with_yield('code_with_yield', sleep_time=2))


if __name__ == "__main__":
    print('start application')
    loop = asyncio.get_event_loop()
    main()
    print('finish application')

    # 
    # task base loop
    # B L O C K I N G - M O D E
    # 
    #   :(
    # 
    # loop.run_until_complete(speak_async())

    # 
    # endless loop
    # 
    loop.run_forever()

    # 
    # close loop
    # never used
    # 
    loop.close()
