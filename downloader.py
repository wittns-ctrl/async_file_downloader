# downloads files

import asyncio
from pathlib import Path

import aiofiles
import aiohttp


class Downloader:

    async def download(self, url, filename):

        for attempt in range(1, 4):

            try:
                print(f"Attempt {attempt}: Downloading {filename}")

                timeout = aiohttp.ClientTimeout(total=10)

                async with aiohttp.ClientSession(timeout=timeout) as client:

                    async with client.get(url) as response:

                        response.raise_for_status()

                        download_folder = Path("downloads")
                        download_folder.mkdir(exist_ok=True)

                        file_path = download_folder / filename

                        downloaded = 0
                        total_size = int(response.headers.get("Content-Length", 0))

                        async with aiofiles.open(file_path, "wb") as file:

                            async for chunk in response.content.iter_chunked(8192):

                                await file.write(chunk)

                                downloaded += len(chunk)

                                if total_size > 0:
                                    average = (downloaded / total_size) * 100
                                    print(f"{filename}, progress: {average:.1f}%")

                print(f"{filename} downloaded successfully!")
                break

            except asyncio.TimeoutError:
                print(f"{filename} has timed out")

                if attempt < 3:
                    print("Retrying in 2 seconds...")
                    await asyncio.sleep(2)
                else:
                    print("Failed to download file after 3 attempts")

            except Exception as error:
                print(f"{filename} failed due to: {error}")

                if attempt < 3:
                    print("Retrying in 2 seconds...")
                    await asyncio.sleep(2)
                else:
                    print("Failed to download file after 3 attempts")