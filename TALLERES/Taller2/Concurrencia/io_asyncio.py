import asyncio
import time
import aiohttp

urls = {
        "imagen": "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800",
        "json": "https://jsonplaceholder.typicode.com/posts/1",
        "csv": "https://raw.githubusercontent.com/plotly/datasets/master/tips.csv",
        "texto": "https://www.gutenberg.org/files/11/11-0.txt",
        "xml": "https://www.w3schools.com/xml/note.xml",
        "pdf": "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
        }  

async def download_site(session, url):
    async with session.get(url) as response:
        await response.read()

async def download_all_sites(sites):
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(download_site(session, url)) for url in sites]
        await asyncio.gather(*tasks, return_exceptions=True)

async def main():
    sites = list(urls.values())
    start_time = time.time()
    await asyncio.create_task(download_all_sites(sites))
    duration = time.time() - start_time
    print(duration)

if __name__ == "__main__":
    asyncio.run(main())