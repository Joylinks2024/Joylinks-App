import asyncio

from loader import get


async def avto_restarter():
    while True:
        a = await get.get_count_users()
        print(a)
        await asyncio.sleep(10)


# async def main():
#     task = asyncio.create_task(avto_restarter())
#     await task

if __name__ == "__main_":
    asyncio.create_task(avto_restarter())
