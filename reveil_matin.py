import subprocess
import pygame
import pygame.mixer
from time import sleep

command = ["amixer", "sset", "Master", "{}%".format(50)]
subprocess.Popen(command)

pygame.init()

crash_sound = pygame.mixer.Sound("clap.wav")


crash_sound.play(loops=100)


print("allo")
sleep(5)
