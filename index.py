from urllib.parse import urlparse
from niconico import NicoNico
from yt_dlp import YoutubeDL
import PySimpleGUI as sg


def start():
    window = setup()
    event, values = window.read()

    isStart = True
    if (event == "bt"):
        isStart = download(values["url"], window)
    if (isStart == False):
        start()


def setup():
    layout = [[sg.Text("動画のURLを入力してください")],
              [sg.Input(key="url")],
              [sg.Button("決定", key="bt")]]
    return sg.Window("VideoDownloadGUI", layout)


def popup(text):
    sg.Popup(text)


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
                popup("ダウンロードが完了しました")

        elif (domain in nicovideo):
            client = NicoNico()
            with client.video.get_video(url) as video:
                video._download_log = lambda x: print(f"[INFO] {x}\r", end="")
                window.close()
                print("ダウンロード中...")
                video.download(f"{video.video.id}.mp4")
                popup("ダウンロードが完了しました")

        else:
            popup("そのURLからはダウンロードできません")
            window.close()
            return False
    except:
        print("エラーが発生しました")
        return False


start()
