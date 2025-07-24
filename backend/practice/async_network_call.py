import time
import asyncio
import aiohttp

async def make_request(session, req_n):
    url = "https://www.google.com/"
    print(f"Making {req_n} network call")
    async with session.get(url) as resp:
        if resp.status == 200:
            texts = await resp.text()
            print(texts)
    
async def main():
    request_count = 10

    async with aiohttp.ClientSession() as session:
        await asyncio.gather(
            *[make_request(session, i) for i in range(request_count)]
        )

loop = asyncio.get_event_loop()
start = time.time()
loop.run_until_complete(main())
end = time.time()
print(f"Time elapsed: ",(end - start))




