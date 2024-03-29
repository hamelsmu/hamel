# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_context.ipynb.

# %% auto 0
__all__ = ['fetch_site_from_sitemap']

# %% ../nbs/01_context.ipynb 2
import os, re, requests
from fastcore.script import call_parse, store_true, Param
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urlparse, urljoin
import pandoc
from pathlib import Path
from requests.exceptions import RequestException
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
from tqdm import tqdm

# %% ../nbs/01_context.ipynb 3
def _sanitize_filename(name):
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        name = name.replace(char, '_')
    # Strip existing file extension if any when markdown is expected
    name = os.path.splitext(name)[0]
    return name

def _html_to_markdown_pandoc(html_content, strip_html=False, media_pth=None):
    p = pandoc.read(source=html_content, format='html')
    md = pandoc.write(p, format='markdown_strict') # options=['--extract-media', media_pth]
    if strip_html: md = re.sub(r'<[^>]*>', '', md)
    return md

def _fetch_and_save(url:str, output_dir:str, to_markdown:bool, strip_html:bool):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        content = response.content  # Assuming binary content to handle non-text files as well

        parsed_url = urlparse(url)
        filename = _sanitize_filename(parsed_url.path.strip('/').replace('/', '_') or 'index')
        media_dir = str(Path(output_dir)/(filename+ '_media'))
        # Determine the file extension based on to_markdown flag
        file_extension = '.md' if to_markdown else '.html'
        filename += file_extension

        filepath = os.path.join(output_dir, filename)
        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        with open(filepath, 'wb' if not to_markdown else 'w', encoding=None if not to_markdown else 'utf-8') as f:
            if to_markdown:
                # Convert HTML to markdown if needed
                content = _html_to_markdown_pandoc(content.decode('utf-8'), media_pth=media_dir, strip_html=strip_html)
            f.write(content)
        return url, None
    except RequestException as e:
        return url, f"HTTP error for URL '{url}': {e}"
    except Exception as e:
        return url, f"Failed to fetch or save URL '{url}': {e}"


def _is_valid_url(url, domain):
    """Check if a URL belongs to the specified domain and is a valid fetch target."""
    parsed_url = urlparse(url)
    return parsed_url.netloc == domain and parsed_url.scheme in ['http', 'https']


def _extract_links(url):
    """
    Extract all hyperlinks from the specified webpage URL.

    Parameters:
    - url (str): The URL of the webpage from which to extract links.

    Returns:
    - set: A set containing all the unique hyperlinks found on the webpage.
    """
    links = set()
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        for link in soup.find_all('a', href=True):
            absolute_link = urljoin(url, link['href'])
            links.add(absolute_link)
    except RequestException as e:
        print(f"HTTP error for URL '{url}': {e}")
    except Exception as e:
        print(f"Failed to extract links from URL '{url}': {e}")
    return links

# %% ../nbs/01_context.ipynb 4
@call_parse
def fetch_site_from_sitemap(url:str, # The site that you want to fetch documents from 
                            output_dir:str, # The output directory to write documents to, 
                            to_html:Param('Write output as HTML instead of markdown.', store_true),
                            strip_html:Param('Strip any embedded HTML in markdown.', store_true)
                           ) :
    """
    Fetch content from the specified URL and save it to the given directory. Saves the content as a markdown file unless `to_html` is True. 
    """
    
    to_markdown = not to_html
    strip_html = strip_html if to_markdown else False
    sitemap_url = urljoin(url, '/sitemap.xml')
    domain = urlparse(url).netloc
    
    def crawl_and_fetch(base_url):
        visited = set()
        to_visit = set([base_url])
    
        with tqdm(total=1, unit='file') as pbar:  # Initialize tqdm with an arbitrary total
            while to_visit:
                current_url = to_visit.pop()
                if current_url not in visited:
                    visited.add(current_url)
                    links = _extract_links(current_url)
                    valid_links = {link for link in links if _is_valid_url(link, domain)}
                    to_visit.update(valid_links - visited)  # Only add links that haven't been visited
                    _fetch_and_save(current_url, output_dir, to_markdown, strip_html)
                    pbar.update(1)  # Update progress bar for each URL processed
                pbar.total = len(visited) + len(to_visit)  # Update the total count
                pbar.refresh() 

    try:
        sitemap_response = requests.get(sitemap_url, timeout=10)
        sitemap_response.raise_for_status()
        sitemap_xml = sitemap_response.text
        # Process sitemap as before...
    except RequestException:
        print(f"Sitemap not found, starting crawl at {url}")
        crawl_and_fetch(url)
    except Exception as e:
        print(f"Unexpected error: {e}")
        return

    try:
        root = ET.fromstring(sitemap_xml)
        namespaces = {'ns': root.tag.split('}')[0].strip('{')}
        urls = [url.text for url in root.findall('ns:url/ns:loc', namespaces)]
    except ET.ParseError as e:
        print(f"Error parsing the XML sitemap: {e}")
        return
    except Exception as e:
        print(f"Unexpected error when parsing sitemap: {e}")
        return

    os.makedirs(output_dir, exist_ok=True)

    tasks = []
    with ThreadPoolExecutor() as executor:
        for url in urls:
            tasks.append(executor.submit(_fetch_and_save, url, output_dir, to_markdown, strip_html))

        for future in tqdm(as_completed(tasks), total=len(tasks), unit='file'):
            url, error = future.result()
            if error:
                print(error)
