#apt update
#apt upgrade

# sudo nano /boot/config.txt
# Uncomment and change dtoverlay row as following (GPIO pin parameter refers to BCM naming for RPI pins):
# dtoverlay=gpio-ir,gpio_pin=17
# sudo reboot
# apt install ir-keytable

#pip install requests --upgrade

apt install ir-keytable

pip3 install -r requirements.in
