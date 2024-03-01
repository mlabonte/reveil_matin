#apt update
#apt upgrade

# sudo nano /boot/config.txt
# Uncomment and change dtoverlay row as following (GPIO pin parameter refers to BCM naming for RPI pins):
# dtoverlay=gpio-ir,gpio_pin=19
# sudo reboot
# apt install ir-keytable

#pip install requests --upgrade

# sudo apt-get install -y libsdl2-mixer-2.0-0

sudo apt install ir-keytable

sudo apt install ffmpeg

sudo pip3 install -r requirements.in

# mv reveilmatin.desktop /home/martin/.config/autostart/reveilmatin.desktop
