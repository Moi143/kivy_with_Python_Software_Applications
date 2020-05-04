from kivy.app import *
from kivy.uix.boxlayout import *
from kivy.core.window import *
from kivy.uix.button import *
class ClacWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.size = (300, 500)
        numb = [7,8,9,'+',4,5,6,'-',1,2,3,'*','.','0','(',')','/']
        self.number = self.ids.number
        numc = ['C','CA']
        self.number = self.ids.number
        for num in numb:
            btn = Button(text = str(num),font_size = '30px',background_color = (1.0,0.0,0.0,1.0))
            btn.bind(on_release = self.echo_numb)
            self.number.add_widget(btn)
        for num in numc:
            btn = Button(text = str(num),font_size = '30px',background_color = (1.0,2.0,2.0,0.6))
            btn.bind(on_release = self.echo_numb)
            self.number.add_widget(btn)
        eq = Button(text = '=',font_size = '30px',background_color = (1.0,2.0,2.0,0.6))
        eq.bind(on_release = self.eval_numb)
        self.number.add_widget(eq)
    def echo_numb(self, instance):
        inputt = self.ids.inputt 
        inputt.text += instance.text
        if instance.text == 'CA':
            inputt.text = ''
        elif instance.text == 'C':
            inputt.text = inputt.text[:-2]
    def eval_numb(self, text):
        inputt = self.ids.inputt
        exp = inputt.text
        eva = eval(exp)
        inputt.text = str(eva)
class ClacApp(App):
    def build(self):
        return ClacWindow()
if __name__ == '__main__':
    ClacApp().run()
