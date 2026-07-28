#start the application

import asyncio
from downloader import Downloader


async def main():
    downloader = Downloader()

    task1 = asyncio.create_task(
    
    downloader.download("https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf","dummy.txt"))

    await task1

    task2 = asyncio.create_task(

    downloader.download("https://docs.google.com/document/d/1zEn9IzlGG2cwaLGG-L7kS2XX4brt6spRDw-gE_NL8AE/edit?tab=t.0","dammy.txt"))

    await task2


if __name__ == "__main__":
    asyncio.run(main())