from googletrans import Translator
import gtts as gt
import os
translator = Translator()
text = input("Enter the text to be translated: ")
src_lang = 'en'
tgt_lang = 'hi'
translation = translator.translate(text, src=src_lang, dest=tgt_lang)
a=translation.text
print(a)
t=a
TamilText=t
tts = gt.gTTS(text=TamilText, lang='ta')
tts.save("Tamil-Audio.mp3")
os.system("Tamil-Audio.mp3")
from IPython.display import Audio
from IPython import display
wn = Audio("Tamil-Audio.mp3", autoplay=True)
display(wn)