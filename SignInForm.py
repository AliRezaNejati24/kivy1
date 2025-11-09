

from kivy.uix.image import Image  
from kivy.uix.label import Label 
from kivy.uix.button import Button 
from kivy.app import App 
from kivy.uix.widget import Widget  
from kivy.core.window import Window  
from kivy.uix.textinput import TextInput

class FormNo1(App):
    def build (self):
        outgo1 = Widget()
        winx = Window.width/2
        winy = Window.height - 120
        img = Image(source="C:/Users/Lenovo/OneDrive/Desktop/profbro1.0.1.jpg", pos = (winx - 530, winy - 190), size = (350, 350))
        label1 = Label (text = "Enter Your Full Name: ", color = (1, 1, 1, 1), pos = (winx - 458, winy - 250), size = (200, 58))
        TheName = TextInput (hint_text = "E.G. MyName is...", multiline = False, pos = (winx - 100, winy - 240), size = (250, 50))
        Label2 = Label (text = "Password Now Please: ", color = (1, 1, 1, 1), pos = (winx - 450, winy - 280), size = (200, 60))
        PasswordIn = TextInput (password = True, hint_text = "E.G. abcd1234 => ********", multiline = False, pos = (winx - 100, winy - 290), size = (250, 50))
        SignInButton = Button (text = "Sign In Now", pos = (winx - 300, winy - 550), size = (150, 50), color = (1, 1, 1, 1))
        Label3 = Label (text = "Have You Pushed This Button Thogh? ", color = (0.3, 0.8, 1, 1), pos = (winx - 150, winy - 500), size = (200, 80), font_size = '23px')

        def on_press_button(instance):
            print ("Congrats! You have just submitted your personal info to me.")
            Label3.text = "OK, Well Now you have. Congrats! You have just submitted your personal info to me."
            Label3.color = (1, 0.2, 0, 1 )

        SignInButton.bind (on_press = on_press_button)   

        outgo1.add_widget(img)
        outgo1.add_widget(label1)
        outgo1.add_widget(TheName)
        outgo1.add_widget(Label2)
        outgo1.add_widget(PasswordIn)
        outgo1.add_widget(SignInButton)
        outgo1.add_widget(Label3)

        return outgo1

FormNo1().run()

