import pytube
from pytube import YouTube
import speech_recognition as sr
import speak
lang='en'
def repeat():
    text="Enter the video link:"
    speak.tts(text, lang)
    yt = YouTube(str(input("Enter the video link: ")))
    text1="Your video is streaming"
    speak.tts(text1, lang)
    videos = yt.streams.all()
    s = 1
    for v in videos:
        print(str(s)+". "+str(v))
        s += 1
    text2="Choose a video Quality"
    speak.tts(text2, lang)
    n = int(input(text2))
    vid = videos[n]
    text3="Enter the Folder where u want to save"
    speak.tts(text3, lang)
    destination = str(input( text3))
    speak.tts("your video is downloading", lang)
    vid.download(destination)
    text4="video Has been supccessfully downloaded"
    speak.tts(text4, lang)
    print("\nvideo Has been supccessfully downloaded")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        text6="Enter yes if u want to download else NO: "
        speak.tts(text6,lang)
        print("Say yes if u want to download else NO:")
        audio = r.listen(source)
    try:
        value_speak = r.recognize_google(audio)
        check=str(value_speak)
        if check=='y' or check =='yes':
            speak.tts("you want to download another video",lang)
            repeat()
        else:
            speak.tts("Thank you for download",lang)
            print("Thank you for download")
    except Exception as e:
        print(e)       
print("Hello Buddy")
repeat()