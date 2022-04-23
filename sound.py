from pygame import mixer

class Sound():
    def __init__(self):
        mixer.init()
        self.bgm = mixer.Sound('./assets/bgm.mp3')
        self.bgm.set_volume(0.1)
        self.pewpew = mixer.Sound('./assets/pewpew.wav')
        self.pewpew.set_volume(1)
        
        
    