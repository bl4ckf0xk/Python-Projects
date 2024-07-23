import requests
from bs4 import BeautifulSoup
import click
import re

def get_all_links(url, depth):
    
    req = requests.get(url)

    if req.status_code != 200:
        print(f'{req.status_code} response code recieved')
        exit(1)
    else:
        soup = BeautifulSoup(req.content.decode(), 'lxml')

    data = []
    links = []
    
    def dup(lists):
        for item in lists:
            match = re.search("(?P<url>https?://[^\s]+)", item)
            if match is not None:
                links.append((match.group("url")))

    for link in soup.find_all('a', href=True):
        data.append(str(link.get('href')))
    
    dup(data)

    if depth != 1:
        for i in range(depth):
            for link in links:
                print(link)
                req = requests.get(link)
                soup = BeautifulSoup(req.content.decode(), 'lxml')
                for link in soup.find_all('a', href=True):
                    data.append(str(link.get('href')))
            print(f'{i} round')
        dup(data)
    for link in links:
        print(link)
    print('All links Found')

@click.command()
@click.option('--url','-u', prompt='Web Url', help='URL of the web page')
@click.option('--lenght','-l', default=0, help='Minimum word lenght')
@click.option('--depth','-d', default=0, help='Crawling Depth')

def main(url, lenght,  depth):
    if depth != 0:
        words = get_all_links(url,depth)
    else:
        pass

    print('End')

if __name__== '__main__':
    main()
