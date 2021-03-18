#packages for speech recognition in python
#apiai,assembiyai,google-cloud-speech,speech-recognition,pocketsphinx,watsondeveloper-cloud,wit
#pip installp pyAudio

import speech_recognition as sr
import webbrowser as wb


r1= sr.Recognizer()
r2=sr.Recognizer()
r3=sr.Recognizer()


with sr.Microphone() as source:
    print('serching akilinn:search youtube')
    print('Speak now')
    audio=r3.listen(source)

if 'capital' in r2.recognize_google(audio):
    r2=sr.Recognizer()
    url='https://www.capitalsyrax.co.ke'
    with sr.Microphone() as source:
        print('search your quesry')
        audio=r2.listen(source)
    try:
        get=r2.recognize_google(audio)
        print(get)
        wb.get().open_new(url+get)
    except sr.UnknownValueError:
        print('error')
    except sr.RequestError as e:
        print('failed'.format(e))