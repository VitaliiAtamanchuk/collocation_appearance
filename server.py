import hug
from hug_middleware_cors import CORSMiddleware

from core.words_appearance import get_words_appearance_dict, fetch_words_appearance
from core.oxf3000 import get_word_link_list, get_rand_words


api = hug.API(__name__)
api.http.add_middleware(CORSMiddleware(api))


@hug.post('/word_appearance')
def word_appearance(words):
    retval = fetch_words_appearance(words)
    return retval


@hug.get('/word_list')
def word_list():
    words = fetch_words_appearance([])
    retval = []
    for word in words:
        retval.append({
            'word': word,
            'link': words[word]['link'],
            'appearance_num': len(words[word]['appearance']),
        })
    return retval


@hug.get('/rand_words')
def word_list(word_num:hug.types.number=10):
    words = get_rand_words(word_num)
    words_appearance = fetch_words_appearance(words)
    retval = []
    for word in words_appearance:
        retval.append({
            'word': word,
            'link': words_appearance[word]['link'],
            'appearance_num': len(words_appearance[word]['appearance']),
        })
    return retval
