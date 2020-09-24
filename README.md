# Pi Loop - Raspberry Pi Headless External Speakers
This is a guide to getting a python script on boot to play audio on 3.5mm speakers on a Raspberry Pi 3 B+ when a monitor isn't connected. Audio on linux is never fun.

## Getting Started
Flash the raspberry pi lite operating system to an SD card, and plug it in. Connect the raspberry pi to an HDMI monitor, a keyboard, and a power source and let it boot.

First, login to the raspberry pi using the default username and password.
```bash
raspberrypi login: pi
Password: raspberry
```

Set up WiFi by adding the following to this file:
```bash
sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
```

```txt
network={
   ssid="Wifi Network Name"
   psk="YourPassword"
}
```

Then run the following. The raspberry pi will restart, and you will need to login again afterwards.
```bash
rfkill unblock wifi
sudo ifconfing wlan0 up
sudo reboot
```

Wait a few moments for your pi to connect to your network. Once you can see an IP address by running the following command, you should be set.
```bash
ifconfig wlan0
> inet 10.0.0.1
```

## Install SSH (Optional)
Installing SSH will allow you to run most commands remotely from your laptop.

```bash
sudo apt-get update && sudo apt-get -y install openssh-server
sudo systemctl enable ssh
sudo service ssh start
```

Find the IP of your raspberry pi.
```bash
ifconfig wlan0
> inet 10.0.0.1
```


## Configure Dependencies and Code

Install dependencies, and then install the example code.
```bash
sudo apt-get update && sudo apt-get -y install mpg321 git
cd /home/pi && git clone https://github.com/rydercalmdown/pi_loop.git
```

Add the following line to `/etc/rc.local` just before the last line that contains `exit 0;`. This will cause the script to run on boot.

```bash
sudo nano /etc/rc.local
```

```txt
python /home/pi/pi_loop/app/app.py > /dev/null &
```


## Configure Audio

Set 3.5mm as your default output.
```bash
sudo raspi-config
```

```txt
Advanced Options > Audio > Headphones 1
```

Also set up auto-login.
```txt
Boot Options > Desktop / CLI > Console Autologin
```
You will need to then reboot.


Once rebooted, the pi should automatically log itself in. Next, set volume to be louder:
```
amixer cset numid=1 900
```

Then, unplug the HDMI cable and restart the raspberry pi.
```bash
sudo reboot
```

The audio should be playing over your 3.5mm speakers, without a monitor connected, when the raspberry pi boots. If it's not, sorry, I can't help you more than this. Linux audio makes me want to throw myself in a volcano.
