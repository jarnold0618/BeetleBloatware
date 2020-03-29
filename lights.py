from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

from gpiozero import OutputDevice

import constant

#change this to change the size of the button layout
widget_size = constant.LightButtons_size

class LightsApp(App):
    headlights_device = OutputDevice(constant.headlights_pin)
    brights_device = OutputDevice(constant.brights_pin)


    def build(self):
        l = Widget()
        box = BoxLayout(orientation='vertical', size=widget_size)
        headlights = Button(text='Headlights',
                        font_size=40,
                        size_hint=(1, 1))
        headlights.bind(on_press=self.toggle_headlights)

        brights = Button(text='Brights',
                        font_size=40,
                        size_hint=(1, 1))
        brights.bind(on_press=self.toggle_brights)


        box.add_widget(headlights)
        box.add_widget(brights)
        l.add_widget(box)
        return l

    def toggle_headlights(self, event):
        # print('Headlights Toggled!')
        self.headlights_device.toggle()

    def toggle_brights(self, event):
        # print('Brights Toggled')
        self.brights_device.toggle()


if __name__=='__main__':
        LightsApp().run()
