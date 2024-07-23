import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def is_valid_url(url):
    """Check if url is valid."""
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def get_all_website_links(url):
    """Returns all URLs that are found on `url` and belong to the same website"""
    # domain name of the URL without the protocol
    domain_name = urlparse(url).netloc
    soup = BeautifulSoup(requests.get(url).content, "html.parser")

    for a_tag in soup.findAll("a"):
        href = a_tag.attrs.get("href")
        if href == "" or href is None:
            # href empty tag
            continue
        # join the URL if it's relative (not absolute link)
        href = urljoin(url, href)
        # remove URL GET parameters, URL fragments, etc.
        href = href.split('?')[0].split('#')[0]
        # skip if it's an external link
        if domain_name not in href:
            continue
        if is_valid_url(href):
            yield href

def crawl(url, max_urls=30):
    """Crawls a web page and extracts all links."""
    local_domain = urlparse(url).netloc
    urls = set()
    urls.add(url)
    visited = set()

    while len(urls) > 0 and len(visited) < max_urls:
        # get next url to visit
        url = urls.pop()
        visited.add(url)
        print(f"Crawling: {url}")  # for debugging

        try:
            for link in get_all_website_links(url):
                if link not in visited and local_domain in link:
                    urls.add(link)
        except Exception as e:
            print(f"Error: {e}")
            continue

    return visited

def generate_sitemap(base_url, output_file="sitemap.txt"):
    """Generate a sitemap and write it to a file."""
    visited_urls = crawl(base_url)
    with open(output_file, "w") as f:
        for url in visited_urls:
            f.write(url + "\n")
    print(f"Sitemap generated and saved to {output_file}")

if __name__ == "__main__":
    # Replace with your local server URL
    base_url = "http://localhost:4000"
    generate_sitemap(base_url)