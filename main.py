import datetime
import wave

import pyjokes
import pyttsx3
import pywhatkit
import os
import buildozer
import speech_recognition as sr
import wikipedia
from kivy.uix.image import Image
import time
import threading
from kivy.app import App
# from kivy.uix.textinput import TextInput
# from kivy.uix.button import Button
# from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.core.audio import SoundLoader
#from kivy.uix.button import Button
#from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager,Screen


class FirstWindow(Screen):
    def run(self):

        try:
            self.ids.image.source = "pressed.png"

            def run1():
                time.sleep(0)
                try:
                    self.run_alexa()
                except:
                    self.add_widget(Label(text="Allow Microphone Permission and Needed Permissions (OR) Try Again ",
                                          size_hint=(None, None),
                                          pos_hint={"x": 0.30, "bottom": 0.50}))

            def image1():
                time.sleep(0)
                self.add_widget(Image(source="liteblue.png",allow_stretch=True,keep_ratio=False,size_hint=(1,.27),pos_hint={"x":0,"y":.43}))
            def one():
                time.sleep(6)
                self.add_widget(Label(text="Speak...",font_size=35,bold=True))

            x = threading.Thread(target=image1)
            x.start()
            y = threading.Thread(target=run1)
            y.start()
            o = threading.Thread(target=one)
            o.start()
        except:
            pass


    def release(self):
        self.ids.image.source = "speak3.png"


    def play(self,file):
        music = SoundLoader.load(file)
        music.play()

    def speak(self, text):
        engine = pyttsx3.init()

        engine.say(text)
        engine.runAndWait()


    def take_command(self):
        try:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                r.energy_threshold = 10000
                print("listening...")
                audio = r.listen(source)
                text = r.recognize_google(audio)
                text = text.lower()
                if 'linda' in text:
                    text = text.replace('linda', '')
                    print(text)
        except:

            pass
        return text


    def run_alexa(self):
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        rate = engine.getProperty('rate')
        engine.setProperty("rate", 140)
        engine.say('Hi, i am linda')
        engine.runAndWait()

        command = self.take_command()
        if 'play' in command:
            song = command.replace('play', '')
            self.speak("playing" + song)
            pywhatkit.playonyt(song)

        elif 'time' in command:
            time1 = datetime.datetime.now().strftime('%H:%M %p')
            self.speak('current time is ' + time1)
            time1 = "current time is " + time1
            self.add_widget(Label(text=time1, font_size=25))

        elif 'search' in command:
            person = command.replace('search', '')
            info = wikipedia.summary(person, 2)
            self.speak(info)
        elif 'hi' in command:
            self.speak('Hey')

        elif 'how are you' in command:
            self.play('bagane.wav')
        elif 'single' in command:
            self.play('poddhune.wav')

            self.speak('yes! rad single')

        elif 'kiss' in command:
            self.play('cchadhuvu.wav')

        elif 'What are you doing' in command:
         self.play('bagane.wav')

        elif 'what are you studying' in command:
            self.play('munnababu1.wav')

        elif 'you are beautiful' in command:
            self.play('thanks.wav')

        elif 'instagram' in command:
            self.play('bagane.wav')

        elif 'joke' in command:
            joke = pyjokes.get_joke()
            self.speak(joke)




        else:
            self.speak(command)
            self.play('nak.wav')
            self.speak('sorry! please say again')
            self.add_widget(Label(text="sorry! please say again", font_size=25
                                  ))

class SecondWindow(Screen):
    pass
class ThirdWindow(Screen):
    pass
class FourthWindow(Screen):
    pass
class FifthWindow(Screen):
    pass
class WindowManager(ScreenManager):
    pass


kv = Builder.load_string("""
<FloatLayout1>:
WindowManager:
    FirstWindow:
    SecondWindow:
    ThirdWindow:
    FourthWindow:
    FifthWindow:
    
<FirstWindow>:
    name: "first"
    
 
    FloatLayout:
        size:root.width,root.height
        background:"white"
        Button:
            text:"f"
            size_hint:(None,None)
            width:130
            height:50
            pos_hint:{"center_x":0.5,"y":.25}
            on_release:
                app.root.current = "second"
                root.manager.transition.direction = "left"                    
        Button:
            width:110
            height:70
            size_hint:(None,None)
            pos_hint:{"x":0.40,"y":0.70}
            on_release: root.release()
            on_press:root.run()
            background_color:0,0,0,0
            Image:
                id: image
                source:"speak3.png"
                center_x:self.parent.center_x
                center_y:self.parent.center_y
        Button:
            text:"suggest"
            size_hint:(None,None)
            width:130
            height:50
            pos_hint:{"y":.35,"bottom":0.6} 
        Button:
            text:"Commands"
            size_hint:(None,None)
            width:130
            height:50
            pos_hint:{"right":1,"y":.35}
            on_release:
                app.root.current = "Third"
                root.manager.transition.direction = "left"
                
                    
            
<SecondWindow>:
    name: "second"
  
 
 
    FloatLayout:
        size:root.width,root.height
        background:"white"
        Button:
            text:"Back"
            size_hint:(None,None)
            width:150
            height:50
            on_release:
                app.root.current = "first"
                root.manager.transition.direction = "right"
        Label:
            text: "You "
            font_size:23
            outline_color:(0,0,0,0)
            bold:True
            color:(0.1,0.7,1,1)
            pos:(0,175)
             
        Label:
            text: "P :"
            font_size:18
            color:(1,1,1,1)
            pos:(-30,145)
        Label:
            text: "G :"
            font_size:18
            color:(1,1,1,1)
            pos:(0,125)
        Label:
            text: "p:"
            font_size:18
            color:(1,1,1,1)
            pos:(0,105)   
            

<ThirdWindow>:
    name: "Third"
  
 
 
    FloatLayout:
        size:root.width,root.height
        background:"white"
        Button:
            text:"Back"
            size_hint:(None,None)
            width:150
            height:50
            on_release:
                app.root.current = "first"
                root.manager.transition.direction = "right"
        Label:
            text: "Normal Commands"
            font_size:23
            outline_color:(0,0,0,0)
            bold:True
            color:(0.1,0.7,1,1)
            pos:(0,175)
             
        Label:
            text: '''"Play" - Play+ your wish'''
            font_size:18
            color:(1,1,1,1)
            
        Label:
            text: '''"Search" - Search+ your wish'''
            font_size:18
            color:(1,1,1,1)
            pos:(0,125)
        Label:
            text: '''"Joke" - Joke'''
            font_size:18
            color:(1,1,1,1)
            pos:(0,105)   
        Label:
            text: '''"Time" - Time'''
            font_size:18
            color:(1,1,1,1)
            pos:(0,105)
        Button:
            text:"More Commands"
            size_hint:(None,None)
            width:150
            height:50
            pos_hint:{"y":.35,"bottom":0.6}
            on_release:
                app.root.current = "Fourth"
                root.manager.transition.direction = "left"        
<FourthWindow>:
    name: "Fourth"
  
 
 
    FloatLayout:
        size:root.width,root.height
        background:"white"
        Button:
            text:"Back"
            size_hint:(None,None)
            width:150
            height:50
            on_release:
                app.root.current = "Third"
                root.manager.transition.direction = "right"
        Label:
            text: "Funny Commands"
            font_size:23
            outline_color:(0,0,0,0)
            bold:True
            color:(0.1,0.7,1,1)
            pos:(0,175)
             
        Label:
            text: '''* "How are you" '''
            font_size:18
            color:(1,1,1,1)
            pos:(-30,145)
        Label:
            text: '''* " you ..?"'''
            font_size:18
            color:(1,1,1,1)
            pos:(0,125)
        Label:
            text: '''* "you"'''
            font_size:18
            color:(1,1,1,1)
            pos:(0,105)   
        Label:
            text: '''"Time" - Time'''
            font_size:18
            color:(1,1,1,1)
            pos:(0,105)
        Button:
            text:"More Commands"
            size_hint:(None,None)
            width:150
            height:50
            pos_hint:{"y":.35,"bottom":0.6}
            on_release:
                app.root.current = "Fifth"
                root.manager.transition.direction = "left"
<FifthWindow>:
    name: "Fifth"
  
 
 
    FloatLayout:
        size:root.width,root.height
        background:"white"
        Button:
            text:"Back"
            size_hint:(None,None)
            width:150
            height:50
            on_release:
                app.root.current = "Fourth"
                root.manager.transition.direction = "right"
        Label:
            text: "Commands"
            font_size:17
            outline_color:(0,0,0,0)
            bold:True
            color:(0.1,0.7,1,1)
            pos:(0,175)
             
        Label:
            text: '''"Play" - Play+ your wish'''
            font_size:18
            color:(1,1,1,1)
            pos:(-30,145)
        Label:
            text: '''"Search" - Search+ your wish'''
            font_size:18
            color:(1,1,1,1)
            pos:(0,125)
        Label:
            text: '''"Joke" - Joke'''
            font_size:18
            color:(1,1,1,1)
            pos:(0,105)   
        Label:
            text: '''"Time" - Time'''
            font_size:18
            color:(1,1,1,1)
            pos:(0,105)
                                                          
""")


Window.clearcolor=(0,0,0,1)
class MyApp(App):
    def build(self):
        self.title= 'app'
        return kv



if __name__=='__main__':
    MyApp().run()

"""
    def play(self, file):
        CHUNK = 1024

        wf = wave.open(file, 'rb')

        p = pyaudio.PyAudio()

        stream = p.open(format=pyaudio.paInt16,
                        channels=2,
                        rate=44100,
                        output=True)
        data = wf.readframes(CHUNK)

        while len(data) > 0:
            stream.write(data)
            data = wf.readframes(CHUNK)

        stream.stop_stream()
        stream.close()
        p.terminate()
             """