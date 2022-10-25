import PySimpleGUI as sg


def setup():
    layout = [[sg.Text("動画のURLを入力してください")],
              [sg.Input(key="url")],
              [sg.Button("決定", key="bt")]]
    return sg.Window("VideoDownloadGUI", layout)


def popup(text):
    sg.Popup(text)
