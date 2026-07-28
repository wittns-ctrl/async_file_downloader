#downloads files

import aiohttp
import aiofiles
from pathlib import Path
import asyncio


class Downloader:
    async def download(self,url,filename):
     for attempt in range(1,4):
      try:
        print(f"Attempt : {attempt} downloading:{filename}")

        timeout = aiohttp.ClientTimeout(total=10)
        async with aiohttp.ClientSession(timeout=timeout) as client:

            async with client.get(url) as response:

                response.raise_for_status()
                content = await response.read()

        download_folder = Path("downloads")
        download_folder.mkdir(exist_ok=True)

        file_path = download_folder/filename

        async with aiofiles.open(file_path,'wb') as file:

            async for chunk in response.content.iter_chunked(8192):
            

               await file.write(chunk)
                   


        print(f"{filename} downloaded successfully")
        break 
      except asyncio.TimeoutError:
         print(f"{filename} has been timed out")   
      except Exception as Error:
        print(f"{filename} has failed due to {Error}") 

        if attempt < 3:
           print("retrying in 2seconds")
           await asyncio.sleep(2)

        else:
           print("failed to download file after 3 attempts")   

                  

                

       
        
   