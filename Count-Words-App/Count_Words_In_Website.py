import requests
from bs4 import BeautifulSoup
import re

PAGE_URL = 'https://academy.hackthebox.com/module/88/section/923'

def get_html_of(url):
    resp = requests.get(url)

    if resp.status_code != 200:
        print(f'{resp.status_code} Http code returned')
        exit(1)

    return resp.content.decode()

def count_occ_in(word_list):
    word_count = {}

    for word in word_list:
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

def get_top_words(all_words):
    occr = count_occ_in(all_words)
    return sorted(occr.items(), key=lambda item: item[1], reverse=True)

all_words = get_all_words(PAGE_URL)
top_words = get_top_words(all_words)

for i in range(10):
    print(top_words[i][0])

# print(top_words)
