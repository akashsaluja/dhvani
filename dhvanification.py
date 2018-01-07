from content import Content
from bingtts import Translator
from pydub import AudioSegment
import os

def dhvanify(content):
    translator = Translator(os.environ['BING_SPEECH_ACCESS_KEY'])
    audioOutputs = []
    finalText = []
    for idx, val in enumerate(content.newsItems):
        val.body = ("Story #%s: " %(idx)) + val.body + "       "
        finalText.append(val.body)
    for idx, text in enumerate(finalText):
        output = translator.speak(text, "en-US", "Female", "riff-16khz-16bit-mono-pcm")
        with open("tmp/file%s.wav"%(idx), "wb") as f:
            f.write(output)
        audioOutputs.append(AudioSegment.from_wav("tmp/file%s.wav"%(idx)))
    
    for idx, snippet in enumerate(audioOutputs):
        if(idx == 0):
            finalAudio = snippet
        else:
            finalAudio = finalAudio + snippet
    finalAudio.export("tmp/final.wav", format="wav")
    return "tmp/final.wav"

    
    
    