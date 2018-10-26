import youtube_dl
from youtube_dl.utils import DEFAULT_OUTTMPL, MaxDownloadsReached


def download_subtitles_from_link(url, max_downloads=10):
    ydl_opts = {
        # 'writeautomaticsub': True,
        'subtitleslangs': ['en'],
        'skip_download': True,
        'outtmpl': './subtitles/' + DEFAULT_OUTTMPL,
        'max_downloads': max_downloads,
        'writeinfojson': True,
        'sleep_interval': 5,
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([url])
        except MaxDownloadsReached:
            pass
