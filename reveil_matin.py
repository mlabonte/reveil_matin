import subprocess
import pygame
import pygame.mixer
from time import sleep


import os
import sys

home_path = '/home/martin/.local/lib/python3.9/site-packages'
if home_path not in sys.path:
	sys.path.append(home_path)

for p in sys.path:
	print(p)

import getch
import time
import logging
import spidev as SPI
sys.path.append("..")
import LCD_1inch14
from PIL import Image,ImageDraw,ImageFont

import RPi.GPIO as GPIO
from signal import pause

GPIO.setmode(GPIO.BCM)   # Set the numbering system to BCM
GPIO.setup(19, GPIO.IN)  # Set BCM Pin 24 as an input

def my_callback(channel):
	print("chan %i = %r" % (channel, GPIO.input(channel)))

#GPIO.add_event_detect(19, GPIO.BOTH, callback=my_callback, bouncetime=300)


print("19 = %r" % GPIO.input(19))
#try:
#    pause()
#except KeyboardInterrupt:
#    GPIO.cleanup()
	
command = ["amixer", "sset", "Master", "{}%".format(50)]
subprocess.Popen(command)

pygame.init()

#crash_sound = pygame.mixer.Sound("clap.wav")


#crash_sound.play(loops=100)



# Raspberry Pi pin configuration:
RST = 27
DC = 25
BL = 18
bus = 0 
device = 0 
logging.basicConfig(level=logging.DEBUG)


import evdev

devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
device = [device for device in devices if device.name == "gpio_ir_recv"].pop()
print(device.path, device.name, device.phys)

#device = evdev.InputDevice('/dev/input/event0')
#print(device)

# Vielle manette videotron - DVD avec nec
# DVD Samsung code 159
# DVD + Select 3 secondes, puis 159, puis DVD

rmkeys = {
	0x50504: "- 1 -",
	0x50505: "- 2 -",
	0x50506: "- 3 -",
	0x50508: "- 4 -",
	0x50509: "- 5 -",
	0x5050a: "- 6 -",
	0x5050c: "- 7 -",
	0x5050d: "- 8 -",
	0x5050e: "- 9 -",
	0x50511: "- 0 -",
	0x50526: "- * -",
	
	0x50518: "rewind",
	0x50519: "play/pause",
	0x5051a: "forward",
	0x50515: "stop",
	0x50514: "record",
	
	0x7070f: "mute",
	0x50532: "last",
	
	0x70707: "Vol++",
	0x7070b: "Vol--",
	0x50559: "chan up",
	0x5051f: "chan down",
	
	0x5052c: "haut",
	0x50513: "droite",
	0x50517: "gauche",
	0x5052d: "bas",
	0x50543: "select",
	
	0x50560: "menu",
	0x5051e: "info",
	0x50531: "exit",
}

try:
    disp = LCD_1inch14.LCD_1inch14()
    # Initialize library.
    disp.Init()
    # Clear display.
    disp.clear()
    #Set the backlight to 100
    disp.bl_DutyCycle(50)
    
    # Create blank image for drawing.
    
    Font1 = ImageFont.truetype("Font/Font00.ttf",50)
    Font2 = ImageFont.truetype("Font/Font00.ttf",35)

    
    image2 = Image.new("RGB", (disp.width, disp.height), "WHITE")
    draw = ImageDraw.Draw(image2)
    
    for event in device.read_loop():
      if event.type == 4:
        if event.value in rmkeys:
            remote_cmd = rmkeys[event.value]
        else:
            remote_cmd = "%x" % event.value
        print(remote_cmd)
    
        logging.info(remote_cmd)
        draw.rectangle([(0,2),(238,133)],fill = "WHITE",outline="BLUE")
        draw.text((1, 15), remote_cmd, font = Font2, fill = "BLACK")
        disp.ShowImage(image2)
    
    getch.getch()
    
    draw.rectangle([(0,23),(170,130)],fill = "WHITE",outline="BLUE")
    draw.text((1, 25), u' 2h58', font = Font1, fill = "RED")
    draw.text((1, 82), u' 2h59', font = Font2, fill = "RED")
    disp.ShowImage(image2)
    
    getch.getch()
    
    disp.module_exit()
    logging.info("quit:")
except IOError as e:
    logging.info(e)    
except KeyboardInterrupt:
    disp.module_exit()
    #GPIO.cleanup()
    logging.info("quit:")
    exit()
