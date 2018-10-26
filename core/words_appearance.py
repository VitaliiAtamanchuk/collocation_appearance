import sys
from os import listdir
from os.path import isfile, join
import json
import re

import webvtt
import nltk
from nltk.stem import PorterStemmer
from nltk.text import Text

from core.oxf3000 import get_rand_words, get_all_words_listdict


def fetch_words_appearance(words):
    data = {}
    with open('appearances.json', 'r') as f:
        data = json.load(f)

    if not words:
        return data

    retval = {}
    for word in data:
        if any([word_link['word'] == word for word_link in words]):
            retval[word] = data[word]
    return retval


def save_all_words_appearances():
    words = get_all_words_listdict()
    data = get_words_appearance_dict(words)
    with open('appearances.json', 'w') as f:
        json.dump(data, f)


def get_words_appearance_dict(words):
    nltk.download('punkt')
    words_appearance = {d['word']: {'link': d['link'], 'appearance': []}
        for d in words}
    subtitle_files = [f  for f in listdir('./subtitles')
        if isfile(join('./subtitles', f)) and f.endswith('.vtt')]
    ps = PorterStemmer()

    for subtitle_file in subtitle_files:
        subtitle_file = join('./subtitles', subtitle_file)
        json_info_file = re.sub('.vtt$', '.json', subtitle_file)
        json_info_file = json_info_file.replace('.en.', '.info.')
        for caption in webvtt.read(subtitle_file):
            word_tokens = nltk.word_tokenize(caption.text.lower())
            s = ''
            info = {}
            tokens = word_tokens
            # for word_token in word_tokens:
            #     tokens.append(ps.stem(word_token))
            with open(json_info_file) as f:
                info = json.load(f)
            for word_app in words_appearance:
                match = set(word_app.lower().split()).issubset(tokens)
                if match:
                    words_appearance[word_app]['appearance'].append({
                        'start': caption.start,
                        'end': caption.end,
                        'title': info['title'],
                        'webpage_url': info['webpage_url'],
                    })
    return words_appearance
