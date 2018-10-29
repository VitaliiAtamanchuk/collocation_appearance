from core.oxf3000 import get_all_wordlist_pages_links, get_rand_words
from core.youtube import download_subtitles_from_link
from core.words_appearance import get_words_appearance_dict, save_all_words_appearances


if __name__ == '__main__':
    # download_subtitles_from_link('https://www.youtube.com/user/Bloomberg/videos', 200)
    # download_subtitles_from_link('https://www.youtube.com/user/TestTubeNetwork/videos', 200)
    # download_subtitles_from_link('https://www.youtube.com/user/JamesESL/videos', 24)
    # get_words_appearance_dict()
    # get_all_wordlist_pages_links()
    save_all_words_appearances()
    print('')
