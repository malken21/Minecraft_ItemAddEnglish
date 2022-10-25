import main

import function


def start():
    window = function.setup()
    event, values = window.read()

    isStart = True
    if (event == "bt"):
        isStart = main.download(values["url"], window)
    if (isStart == False):
        start()


start()
