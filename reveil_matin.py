import subprocess
import pygame
import pygame.mixer
from io import BytesIO
from gtts import gTTS
from time import sleep


import os

import time
import logging

class ReveilMatin(object):
    volume = 50
    
    def __init__(self):
        pygame.init()

    def update_volume(self):
        command = ["amixer", "sset", "Master", "{}%".format(self.volume)]
        subprocess.Popen(command)

    def monte_le_son(self):
        if self.volume <= 95:
            self.volume += 5
        self.update_volume()

    def baisse_le_son(self):
        if self.volume >= 5:
            self.volume -= 5
        self.update_volume()

    def parle(self, texte):
        tts = gTTS(texte, lang='fr', tld='ca')
        #tts.save('hello.mp3')
        mp3_fp = BytesIO()
        tts.write_to_fp(mp3_fp)
        mp3_fp.seek(0)
        pygame.mixer.music.unload()
        pygame.mixer.music.load(mp3_fp, "mp3")
        pygame.mixer.music.play()

    def play(self, filename="Sail.mp3"):
        # ffmpeg -i Sail.m4a Sail.mp3
        #f = open("sail.mp3", "rb")
        #buf = BytesIO(f.read())
        #buf.seek(0)
        pygame.mixer.music.unload()
        pygame.mixer.music.load("../Music/%s" % filename)
        pygame.mixer.music.play()
        
    def stop(self):
        pygame.mixer.music.stop()

_reveil_matin = None

def get_reveil_matin():
    global _reveil_matin
    if _reveil_matin is None:
        _reveil_matin = ReveilMatin()
    return _reveil_matin

if __name__ == '__main__':
    rm = get_reveil_matin()
    #rm.parle("coucou Martin")
    #time.sleep(3)
    rm.play()
    time.sleep(15)
        #mp3_fp.seek(0)
        #pygame.mixer.music.load(mp3_fp)#, "mp3")
        #pygame.mixer.music.play()

        
