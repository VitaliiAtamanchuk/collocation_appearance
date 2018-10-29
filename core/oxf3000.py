import csv
import time
import random

import requests
from bs4 import BeautifulSoup


def get_all_wordlist_pages_links():
    sections_links = [
        'https://www.oxfordlearnersdictionaries.com/us/wordlist/english/oxford3000/Oxford3000_A-B/'
    ]
    page = get_page(sections_links[0])
    for link in page.select('#entries-selector a'):
        sections_links.append(link.get('href'))

    word_link_list = []
    pages_links = sections_links[:]
    for section_link in sections_links:
        page = get_page(section_link)
        word_link_list.extend(get_word_lists_from_page(page))
        while page.select('.paging_links')[0].select('li a')[-1].get_text() == '>':
            next_page_link = page.select('.paging_links')[0].select('li a')[-1].get('href')
            page = get_page(next_page_link)
            word_link_list.extend(get_word_lists_from_page(page))
            pages_links.append(next_page_link)

    with open('word_link.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ',
            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for word_link in word_link_list:
            writer.writerow(word_link)


def get_page(url):
    print(f'GETTING PAGE {url}')
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    result = requests.get(url, headers=headers)
    content = result.content
    soup = BeautifulSoup(content, 'html.parser')
    time.sleep(4)
    return soup


def get_word_lists_from_page(page):
    retval = []
    for word in page.select('#entrylist1 li a'):
        name = word.get_text()
        link = word.get('href')
        retval.append((
            name, link
        ))
    return retval


def get_word_link_list():
    rows = []
    with open('word_link.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            rows.append({
                'word': row[0],
                'link': row[1]
            })
    return rows


def get_rand_words(num=10):
    rows = []
    with open('word_link.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            rows.append(row)

    retval = []
    for i in range(num):
        word, link = random.choice(rows)
        if word[-2:] in [' 1', ' 2']:
            word = word[:-2]
        retval.append({
            'word': word,
            'link': link,
        })
    return retval


def get_all_words_listdict():
    print('helloo')
    rows = []
    with open('word_link.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            rows.append(row)

    retval = []
    for row in rows:
        retval.append({
            'word': row[0],
            'link': row[1],
        })
    return retval
