import speech_recognition


def speech_tr():
    mic = speech_recognition.Microphone()
    kayit = speech_recognition.Recognizer()
    with mic as ses_dosyasi:
        print("ses kaydı başladı")
        kayit.adjust_for_ambient_noise(ses_dosyasi)
        ses = kayit.listen(ses_dosyasi)
        try:
            return kayit.recognize_google(ses_dosyasi,language="tr-TR")

        except:
            return "Nedediğinizi Anlamadım"


def speech_en():
    mic = speech_recognition.Microphone()
    kayit = speech_recognition.Recognizer()
    with mic as ses_dosyasi:
        print("ses kaydı başladı")
        kayit.adjust_for_ambient_noise(ses_dosyasi)
        ses = kayit.listen(ses_dosyasi)
        try:
            return kayit.recognize_google

        except:
            return "Nedediğinizi Anlamadım"