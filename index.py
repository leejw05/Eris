import os
from gtts import gTTS
import speech_recognition as sr
import pyautogui
import pyperclip
import re

def speak(text ,lang="ko", speed=False):
    tts = gTTS(text=text, lang=lang , slow=speed)
    tts.save("./tts.mp3")
    os.system("afplay " + "./tts.mp3")

def write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("command","v")
    pyautogui.write(" ")
    return

def autoWrite():
    speak("타이핑을 시작합니다")
    while True:
        with mic as source:
            audio = Recognizer.listen(source ,phrase_time_limit=1)
        try:
            data = Recognizer.recognize_google(audio, language="ko")
        except:
            speak("제가 이해하지 못하는 말이에요")
            continue
        if data.find("이제 꺼") > -1:
            speak("타이핑을 종료합니다")
            return main()
        else:
            write(data)


def main():
    speak("음성인식 시작")
    while True:
        with mic as source:
            audio = Recognizer.listen(source)
        try:
            data = Recognizer.recognize_google(audio, language="ko")
        except:
            speak("제가 이해하지 못하는 말이에요")
            continue
        print(data)
        if "에리스" in data or "엘리스" in data or "앨리스" in data:
            speak("네")  
        elif "라고 해 봐" in data:
            text = data.replace("라고 해 봐","")
            speak(text)
        elif "타이핑 해" in data:
            return autoWrite()
        elif "이제 꺼" in data or "이제 가" in data or "잘가" in data:
            speak("종료합니다")
            return
        else:
            speak("다시 불러주세요")

Recognizer = sr.Recognizer()
mic = sr.Microphone()
main()

