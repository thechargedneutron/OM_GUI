from kivy.uix.button import Button
from kivy.properties import NumericProperty
from UnitOP import UnitOP
from Mixer import Mixer
from MatStrm import Stream
from Flash import Flash

class SMixer(Button):
    included = NumericProperty(0)
    UO = Mixer
    def __init__(self, **kwargs):
        super(SMixer, self).__init__(**kwargs)
        self.size_hint = None, None
        self.size = (52, 87)
        self.background_normal = 'Mixer1.png'
        self.bind(on_press=self.Pressed)

    def Pressed(self, instance):
            self.included = self.included + 1

class SMatStrm(Button):
    included = NumericProperty(0)
    UO = Stream
    def __init__(self, **kwargs):
        super(SMatStrm, self).__init__(**kwargs)
        self.size_hint = None, None
        self.size = (30, 15)
        self.background_normal = 'MatStm.png'
        self.bind(on_press=self.Pressed)

    def Pressed(self, instance):
        self.included = self.included + 1

class SFlash(Button):
    included = NumericProperty(0)
    UO = Flash
    def __init__(self, **kwargs):
        super(SFlash, self).__init__(**kwargs)
        self.size_hint = None, None
        self.size = (50, 134)
        self.background_normal = 'Flash.png'
        self.bind(on_press=self.Pressed)

    def Pressed(self, instance):
        self.included = self.included + 1


