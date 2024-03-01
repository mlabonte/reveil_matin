import threading
import evdev
import logging
from select import select

from ecran import get_ecran
from time import time

devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
try:
	device = [device for device in devices if device.name == "gpio_ir_recv"].pop()
except KeyError:
	logging.error("dtoverlay=gpio-ir,gpio_pin=19 -- manquant ??")
	
print(device.path, device.name, device.phys)

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

_continuer = True

def start():
    devices = {
        device.fd: device,
    }
    last_command = time()
    while _continuer:
        r, w, x = select(devices, [], [], 1)
        if device.fd in r:
            for event in device.read():
                if event.type == 4 and (time() - last_command > .25):
                    last_command = time()
                    if event.value in rmkeys:
                        remote_cmd = rmkeys[event.value]
                    else:
                        remote_cmd = "%x" % event.value
                    print(remote_cmd)
                    get_ecran().afficher_text(remote_cmd)

def lancer_remote():
    t = threading.Thread(target=start)
    t.start()

def stopper_remote():
    global _continuer
    _continuer = False

if __name__ == '__main__':
    lancer_remote()
    input("Enter pour quitter")
    stopper_remote()

