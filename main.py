import asyncio

async def some_function(n):
    print(f'Sleeping for {n} seconds ...')
    r = await asyncio.sleep(n)
    print(f'Waking up after {n} seconds ...')
    return n

async def main():
    print('GATHER BEGIN')
    values = await asyncio.gather(some_function(2), some_function(5), some_function(3),)
    print('GATHER END')
    print(f'Final values: {values}')

print('START')
asyncio.run(main())
print('END')

"""
Logs

START
GATHER BEGIN
Sleeping for 2 seconds ...
Sleeping for 5 seconds ...
Sleeping for 3 seconds ...
Waking up after 2 seconds ...
Waking up after 3 seconds ...
Waking up after 5 seconds ...
GATHER END
Final values: [2, 5, 3]
END
"""
