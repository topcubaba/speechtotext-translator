from google_trans_new import google_translator
import speech_recognition as sr

translator = google_translator()
R = sr.Recognizer()
loop = True
while loop:
    audio_data = ''
    with sr.Microphone() as source:
        R.adjust_for_ambient_noise(source)
        print("PLEASE TALK")
        audio_data = R.record(source, duration=5)
        try:
            print("WORKING...")
            speech = R.recognize_google(audio_data, language="tr-TR")
            print(speech)
            print("TRANSLATING")
            output = translator.translate(speech,lang_tgt='en')
            print(output)
        except:
            pass
