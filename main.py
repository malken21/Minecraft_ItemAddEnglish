from urllib.parse import urlparse
from yt_dlp import YoutubeDL
from niconico import NicoNico

import function


def download(url, window):
    try:
        domain = urlparse(url).netloc

        youtube = ["youtube.com", "www.youtube.com",
                   "youtu.be", "music.youtube.com"]

        nicovideo = ["www.nicovideo.jp", "nicovideo.jp", "nico.ms"]

        if (domain in youtube):
            with YoutubeDL({'format': 'mp4'}) as ytdl:
                window.close()
                print("ダウンロード中...")
                ytdl.download(url)
                function.popup("ダウンロードが完了しました")

        elif (domain in nicovideo):
            client = NicoNico()
            with client.video.get_video(url) as video:
                window.close()
                print("ダウンロード中...")
                video.download(f"{video.video.id}.mp4")
                function.popup("ダウンロードが完了しました")

        else:
            function.popup("そのURLからはダウンロードできません")
            window.close()
            return False
    except:
        print("エラーが発生しました")
        return False
