#start the application

import asyncio
from downloader import Downloader


async def main():
    downloader = Downloader()
    await downloader.download("https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf","dummy.txt")


if __name__ == "__main__":
    asyncio.run(main())