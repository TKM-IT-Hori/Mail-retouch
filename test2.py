import speech_recognition

r = speech_recognition.Recognizer()
with speech_recognition.AudioFile("itou.wav") as source:
    audio = r.record(source)
s=(r.recognize_google(audio, language='ja-JP'))
print(s)