import asyncio
import aiohttp
import argparse
import os


async def download_site(url, session, dir_path, i):
    async with session.get(url) as response:
        r = await response.read()
        with open(os.path.join(dir_path, f'{i}.jpeg'), 'wb') as f:
            f.write(r)


async def download_all_sites(n, dir_path):
    os.makedirs(dir_path, exist_ok=True)
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(n):
            task = asyncio.create_task(download_site('https://picsum.photos/200/300', session, dir_path, i))
            tasks.append(task)

        return await asyncio.gather(*tasks)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', type=int, help='files number')
    parser.add_argument('-d', help='save directory path')
    args = parser.parse_args()

    asyncio.run(download_all_sites(args.n, args.d))

    # python easy.py -n 10 -d "./res"
