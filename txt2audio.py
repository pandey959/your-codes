# Text into audio

from playsound import playsound
from gtts import gTTS

audio='speech.mp3'
language='en'
sp=gTTS(text=input('Enter the text:\n'), lang=language,slow=False)
sp.save(audio)
playsound(audio)