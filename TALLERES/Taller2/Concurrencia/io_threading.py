import concurrent.futures
import requests
import threading
import time

urls = {
        "imagen": "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800",
        "json": "https://jsonplaceholder.typicode.com/posts/1",
        "csv": "https://raw.githubusercontent.com/plotly/datasets/master/tips.csv",
        "texto": "https://www.gutenberg.org/files/11/11-0.txt",
        "xml": "https://www.w3schools.com/xml/note.xml",
        "pdf": "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
        }

thread_local = threading.local()

def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session

def download_site(url):
    session = get_session()
    with session.get(url) as response:
        return len(response.content)

def download_all_sites(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_site, sites)

def main():
    sites = list(urls.values())
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(duration)

if __name__ == "__main__":
    main()