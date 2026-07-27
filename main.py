#start the application

import asyncio
from downloader import Downloader


async def main():
    downloader = Downloader()
    await downloader.download()


if __name__ == "main":
    asyncio.run(main())