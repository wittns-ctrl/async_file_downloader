#downloads files

import aiohttp
import aiofiles
from pathlib import Path


class Downloader:
    async def download(self,url,filename):
     try:
        async with aiohttp.ClientSession() as client:

            async with client.get(url) as response:
                
                response.raise_for_status()
                content = await response.read()

        download_folder = Path("downloads")
        download_folder.mkdir(exist_ok=True)

        file_path = download_folder/filename

        async with aiofiles.open(file_path,'wb') as file:

            await file.write(content)


        print(f"{filename} downloaded successfully")    
     except Exception as Error:
        print(f"{filename} has failed due to {Error}")            

                

       
        
   