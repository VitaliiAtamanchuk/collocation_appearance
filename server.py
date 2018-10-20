import hug
from hug_middleware_cors import CORSMiddleware

from core.words_appearance import get_words_appearance_dict
from core.oxf3000 import get_word_link_list, get_rand_words


api = hug.API(__name__)
api.http.add_middleware(CORSMiddleware(api))


@hug.post('/word_appearance')
def word_appearance(words):
    retval = get_words_appearance_dict(words)
    return retval


@hug.get('/word_list')
def word_list():
    retval = get_word_link_list()
    return retval


@hug.get('/rand_words')
def word_list(word_num:hug.types.number=10):
    retval = get_rand_words(word_num)
    return retval

