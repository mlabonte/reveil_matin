import os
import logging
import spidev as SPI
from time import sleep
from threading import RLock
print("import ecran")
import LCD_1inch14
print("import LCD_1inch14")
from PIL import Image,ImageDraw,ImageFont

lock = RLock()

logging.basicConfig(level=logging.DEBUG)


class Ecran(object):
    # Raspberry Pi pin configuration:
    RST = 27
    DC = 25
    BL = 18
    bus = 0 
    device = 0 

    def __init__(self):
        print("constructeur")
        self.disp = LCD_1inch14.LCD_1inch14()
        # Initialize library.
        self.disp.Init()
        self.turn_on()
        self.image = Image.new("RGB", (self.disp.width, self.disp.height), "WHITE")
        self.Font1 = ImageFont.truetype("Font/Font00.ttf",50)
        self.Font2 = ImageFont.truetype("Font/Font00.ttf",35)
        self.draw = ImageDraw.Draw(self.image)
    
    def afficher_text(self, text):
        with lock:
            # Create blank image for drawing.
            self.draw.rectangle([(0,2),(238,133)],fill = "WHITE",outline="BLUE")
            self.draw.text((1, 15), text, font = self.Font2, fill = "BLACK")
            self.disp.ShowImage(self.image)

    def afficher_image(self, filename):
        with lock:
            logging.info("show image")
            image = Image.open('../Pictures/%s' % filename)	
            self.disp.ShowImage(image)

    def turn_off(self):
        with lock:
            self.disp.clear()
            self.disp.bl_DutyCycle(0) # 100?
    
    def turn_on(self):
        with lock:
            # Clear display.
            self.disp.clear()
            #Set the backlight to 100
            self.disp.bl_DutyCycle(50)

    def close(self):
        self.disp.module_exit()

_ecran = None

def get_ecran():
    with lock:
        global _ecran
        if _ecran is None:
            _ecran = Ecran()
        return _ecran

if __name__ == '__main__':
    ecran = get_ecran()
    ecran.afficher_text("Allo")
    text = input("entrer du texte: ")
    ecran.afficher_text(text)
    sleep(5)
    ecran.afficher_image('LCD_1inch14.jpg')
    sleep(5)
    ecran.turn_off()
    sleep(2)
    ecran.close()
