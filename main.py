from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        self.button = Button(text='Натисни мене')
        self.button.bind(on_press=self.change_text)
        return self.button

    def change_text(self, instance):
        self.button.text = 'Це І. Михайла!'

if __name__ == '__main__':
    MyApp().run()
