from aiohttp import ClientSession
import asyncio

async def get_character(session, url: str) -> str:
    response = await session.get(url)
    character = await response.json()
    return character['name']
    

async def main():
    async with ClientSession() as session:
        task = []
        for numbre in range(1, 3):
            url = f'https://rickandmortyapi.com/api/character/{numbre}'
            task.append(asyncio.create_task(get_character(session, url=url)))
        
        response = await asyncio.gather(*task)
        print(response)

asyncio.run(main())