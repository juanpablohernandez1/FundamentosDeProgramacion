import requests
import multiprocessing
import time

session = None

def set_global_session():
    global session
    if not session:
        session = requests.Session()

def download_site(url):
    with session.get(url) as response:
        return f"Read {len(response.content)} from {url}"

def download_all_sites(sites):
    with multiprocessing.Pool(initializer=set_global_session) as pool:
        results = pool.map(download_site, sites)
    for r in results:
        print(r)

def main():
    urls = {
        "imagen": "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800",
        "json": "https://jsonplaceholder.typicode.com/posts/1",
        "csv": "https://raw.githubusercontent.com/plotly/datasets/master/tips.csv",
        "texto": "https://www.gutenberg.org/files/11/11-0.txt",
        "xml": "https://www.w3schools.com/xml/note.xml",
        "pdf": "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
    }
    
    sites = list(urls.values())
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(duration)

if __name__ == "__main__":
    main()