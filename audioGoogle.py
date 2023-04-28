from gtts import gTTS

tts = gTTS(text='This is a test how natural the speech synthesis is on the gtts model', lang='en', tld='us')
tts.save("audio-1.mp3")