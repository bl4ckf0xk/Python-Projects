import requests
from bs4 import BeautifulSoup
import click
import re
from urllib.parse import urljoin

def get_all_links(url, depth):
    links = []
    data = [url]

    for i in range(depth):
        new_data = []
        for link in data:
            try:
                req = requests.get(link)
                req.raise_for_status()
            except requests.RequestException as e:
                print(f'Error fetching {link}: {e}')
                continue

            soup = BeautifulSoup(req.content.decode(), 'lxml')
            for a_tag in soup.find_all('a', href=True):
                href = a_tag.get('href')
                # Resolve relative URLs to absolute URLs
                absolute_url = urljoin(link, href)
                if absolute_url.startswith(('http://', 'https://')) and absolute_url not in links:
                    new_data.append(absolute_url)
                    links.append(absolute_url)

        data = new_data
        print(f'{i+1} round')

    for link in links:
        print("Found Links:", link)

    return links

def count_occ_in(word_list, min_length):
    word_count = {}
    for word in word_list:
        if len(word) < min_length:
            continue
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

def get_html_of(links):
    data = []
    for link in links:
        try:
            req = requests.get(link)
            req.raise_for_status()
        except requests.RequestException as e:
            print(f'Error fetching {link}: {e}')
            continue
        data.append(req.content.decode())
    return data

def get_all_words(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    raw_text = soup.get_text()
    return re.findall(r'\w+', raw_text)

def get_top_words(all_words, min_length):
    occr = count_occ_in(all_words, min_length)
    return sorted(occr.items(), key=lambda item: item[1], reverse=True)

@click.command()
@click.option('--url', '-u', prompt='Web URL', help='URL of the web page')
@click.option('--length', '-l', default=0, help='Minimum word length')
@click.option('--depth', '-d', default=0, help='Crawling Depth')
def main(url, length, depth):
    links = []
    if depth != 0:
        links = get_all_links(url, depth)
    else:
        links = [url]

    all_words = []
    html_data = get_html_of(links)
    for data in html_data:
        words = get_all_words(data)
        all_words.extend(words)

    top_words = get_top_words(all_words, length)
    for word, count in top_words[:10]:
        print(f'{word}: {count}')

    print('End')

if __name__ == '__main__':
    main()

