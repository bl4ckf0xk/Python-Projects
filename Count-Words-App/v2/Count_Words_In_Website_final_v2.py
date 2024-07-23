import requests
from bs4 import BeautifulSoup
import re
import click
import time

def get_html_of(url):
    resp = requests.get(url)

    if resp.status_code != 200:
        print(f'{resp.status_code} Http code returned')
        exit(1)

    return resp.content.decode()

def count_occ_in(word_list,min_lenght):
    word_count = {}

    for word in word_list:
        if len(word) < min_lenght:
            continue
        if word not in word_count:
            word_count[word] = 1

        else:
            curr_count = word_count.get(word)
            word_count[word] = curr_count + 1
    return word_count

def get_all_words(url):
    html = get_html_of(url)
    soup = BeautifulSoup(html, 'html.parser')
    raw_text = soup.get_text()
    return re.findall(r'\w+', raw_text)

def get_top_words(all_words,min_lenght):
    occr = count_occ_in(all_words, min_lenght)
    return sorted(occr.items(), key=lambda item: item[1], reverse=True)

def write_to_file(output, top_words):
    with open(f'{output}.txt', 'w') as wr:
        wr.write(str(top_words))
    wr.close()

def get_link(url, depth, lenght):

    for i in range(depth):
        html = get_html_of(url)
        soup = BeautifulSoup(html, 'lxml')
        data = []
        links = []

        def remove_dup(list):
            for item in list:
                match = re.search("(?P<url>https?://[^\s]+)", item)
                if match is not None:
                    links.append((match.group("url")))

        for link in soup.find_all('a', href=True):
            data.append(str(link.get('href')))
        flag = True
        remove_dup(data)

        for url in links:
            print(url)
            the_words = get_all_words(url)
            top_words = get_top_words(the_words, lenght)

            listlen = len(top_words)
            #for i in range(listlen):
                #print(top_words[i][0])

# ---------------------------------------------------------------------------

@click.command()
@click.option('--url', '-u', prompt='Web Url', help='URL of the webpage')
@click.option('--lenght', '-l', default=0, help='Minimum word lenght')
@click.option('--output', '-u', prompt='File Name', help='File name to be saved')
@click.option('--depth', '-d', default=0, help='Crawling Depth')

# ---------------------------------------------------------------------------

def main(url, lenght, output, depth):
    page_url = 'https://academy.hackthebox.com/module/88/section/924'
    the_words = get_all_words(url)
    top_words = get_top_words(the_words, lenght)
    write_to_file(output, top_words)
    if depth != 0:
        for i in range(depth):
            get_link(page_url,depth,lenght)
    else:
        pass

    #for i in range(10):
        #print(top_words[i][0])

if __name__ == '__main__':
    main()
