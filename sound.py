from pygame import mixer

class Sound():
    def __init__(self):
        mixer.pre_init(22050, -16, 1, 64)
        mixer.init()
        
        self.bgm = mixer.Sound('./assets/bgm.mp3')
        self.bgm.set_volume(0.08)
        
        self.pewpew = mixer.Sound('./assets/pewpew.wav')
        self.pewpew.set_volume(0.3)
        
        self.boom = mixer.Sound('./assets/boom.wav')
        self.boom.set_volume(0.05)
        
        # collect all the sounds you need
        # level up
        # lose a live
        # game over
        
    