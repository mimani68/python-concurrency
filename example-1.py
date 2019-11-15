import asyncio
from time import sleep

async def speak_async():
    print('1')
    sleep(3)
    print('2')


print('start application')
loop = asyncio.get_event_loop()
asyncio.ensure_future(speak_async('a'))
print('finish application')


# 
# task base loop
# B L O C K I N G - M O D E
# 
# loop.run_until_complete(speak_async())

# 
# endless loop
# 
loop.run_forever()



