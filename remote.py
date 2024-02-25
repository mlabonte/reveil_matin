import evdev

device = evdev.InputDevice('/dev/input/event0')
print(device)

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

for event in device.read_loop():
    if event.type == 4:
        if event.value in rmkeys:
            print(rmkeys[event.value])
        else:
            print("%x" % event.value)

