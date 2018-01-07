from content import Content
from bingtts import Translator
import os

def dhvanify(content):
    translator = Translator(os.environ['BING_SPEECH_ACCESS_KEY'])
    print(os.environ['BING_SPEECH_ACCESS_KEY'])
    audioOutputs = []
    finalText = []
    for idx, val in enumerate(content.newsItems):
        val.body = ("Story #%s: " %(idx)) + val.body + "       "
        finalText.append(val.body)
    for newsItem in finalText:
        print(newsItem)
    output  = translator.speak(finalText[0], "en-US", "Female", "riff-16khz-16bit-mono-pcm")
    with open("file.wav", "wb") as f:
        f.write(output)
    