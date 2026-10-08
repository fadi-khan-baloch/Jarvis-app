from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from plyer import tts

brain = {"light on":"torch_on"}
memory = {"ghar":[]}

def speak(t):
    try:
        tts.speak(t)
    except:
        print(t)

class JarvisUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)
        self.label = Label(text="JARVIS Offline")
        self.input = TextInput(hint_text="bolo: light on")
        self.btn = Button(text="EXECUTE")
        self.log = Label(text="Ready")
        self.add_widget(self.label)
        self.add_widget(self.input)
        self.add_widget(self.btn)
        self.add_widget(self.log)
        self.btn.bind(on_press=self.run)

    def run(self, _):
        txt = self.input.text.lower()
        if "yaad rakho" in txt:
            item = txt.replace("yaad rakho","")
            memory["ghar"].append(item)
            speak("yaad rakh liya " + item)
            self.log.text = "Yaad: " + item
        elif "light" in txt:
            speak("Light on kar di boss")
            self.log.text = "Torch ON"
        elif "msg likho" in txt:
            speak("Msg likh diya boss")
            self.log.text = "Msg done"
        else:
            brain[txt] = "custom"
            speak("Seekh liya")
            self.log.text = "Learned: " + txt

class JarvisApp(App):
    def build(self):
        return JarvisUI()

JarvisApp().run()
      
