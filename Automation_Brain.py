import open_App
import web_open
import pyautogui as gui
from play_music_yt import play_music_on_youtube
from TextToSpeech import TTS8
from play_music_spotify import play_music_on_spotify

def close():
    gui.hotkey('alt','f4')
def Open_Brain(text):
    
    if "website" in text  or "open website named" in text:
        text = text.replace("open ","").strip()
        text = text.replace("website","").strip()
        text = text.replace("open website named","").strip()
        web_open.openweb(text)
        
    else:
         text = text.replace("open","").strip()
         text = text.replace("app","").strip()
        
         open_App.open_App(text)    
        
while True:
    x = input("Hukum mere akka : ")  
    Open_Brain(x)  
    

def Auto_main_brain(text):
    if text.startswitch("open"):
         Open_Brain(text)
    
    elif "close" in taxt:
        close()
        
    elif "play music" in text or "play music on youtube"   in text:
        
        TTS8.speak("which song do you want to play sir.")
        x = input()
        play_music_on_youtube(x)
        
    elif "play some music" in text or "play music on spotify"  in text:
         TTS8.speak("which song do you want to play sir.")
         
         x = input()
         play_music_on_spotify(x)
         
    else:
        pass
    
while True:
    x = input("x :")
    Auto_main_brain(x)     
    