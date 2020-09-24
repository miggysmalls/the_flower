# The Flower


The Flower will by a new adventure in servos and sensors in the python language. Below are the requirements, both the hardware and software requirements.  Don't worry, this should be painless.  This repo assumes you have already loaded on a microSD card the operating system (OS) of your choice, made necessary updates, enabled ssh communication and enabled the I2C interface on the raspberry pi zero W/WH.  If you want this guide to have those steps please open an issue in this repo and I will add those steps.

# Requirements:
## Hardware
##### Raspberry pi zero W or WH. 
* The difference between `W` and `WH` version is the `WH` comes with pre-soldered GPIO header. This is will save you time and is worth the slight increase in cost. If you want to solder in the header yourself you can but you won't be save much money and it will be 40 closely spaced pins.  I'm not presenting all the options.  Amazon has them far more expensive and the only other place I've seen it at this price is in MicroCenter and that is an in store only purchase.  MicroCenter is my choice as I can drive to one of their locations.  
    * https://www.adafruit.com/product/3708
    
    
##### Server Controller
* Servo Driver HAT for Raspberry Pi, 16-Channel, 12-bit, I2C Interface.  I selected the board below in the link but there are other options out there.  If you don't subscribe to the hat philosophy and are not using the header you can find boards that do not have the headers pre-soldered in place as well.
    * https://www.makerfocus.com/products/pwm-servo-motor-driver-iic-module-for-raspberry-pi

## Software
#### Assumptions: git is already installed 
`sudo apt-get install cmake git`

Now that the above hardware has been setup you will need to clone the this repo to complete the setup. Some of the dependencies for this project require python version 3.7.4 or higher.  The raspberry pi comes with version 3.7.3 by default so you will need to upgrade python before you can get started. Don't worry though, clone the repo first because there are scripts that will handle all this for you. 

`git clone git@github.com:miggysmalls/the_flower.git`

When this is completed.

`cd the_flower`

First let's get the right version of python.

`source setup_python_3.7.4.sh`

Next we want to get our python virtual env started.

`source setup_python_venv.sh`

Now to bring everything up to speed you will install all the required dependencies with pip.

`pip install -r requirements.txt`

When this is completed you are ready to rock and roll. 

## Optionally
#### Remotely Controlling Your Raspberry Pi:
After the you have finished your initial setup and your raspberry pi is on the network you can get the IP address of your pi.  You do this by using the command `ifconfig`.  You should see an output similar to this. In this example you see the `lo` inet is set to `127.0.0.1` indicating that the ethernet is not being used. The `wlan0` has a value for its inet of `192.168.1.116`.  This is the value you are looking for so you can remotely control the pi over the network with out having a keyboard, mouse, or monitor plugged into it. 
```log
(venv) pi@raspberrypi:~/git/the_flower $ ifconfig
lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 6  bytes 408 (408.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 6  bytes 408 (408.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

wlan0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.1.116  netmask 255.255.255.0  broadcast 192.168.1.255
        inet6 fe80::e2a8:482a:c343:7346  prefixlen 64  scopeid 0x20<link>
        inet6 2600:6c50:437f:ff20:7a6:1b81:4c62:bdc6  prefixlen 64  scopeid 0x0<global>
        ether b8:27:eb:21:dd:a2  txqueuelen 1000  (Ethernet)
        RX packets 42907  bytes 3003561 (2.8 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 49426  bytes 9536461 (9.0 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

From any other desktop/laptop/mobile device you can `ssh`into the raspberry pi. You can issue the following command using the example above to the find the valid inet value: `ssh pi@192.168.1.116`.  You will be prompted for the password.  Enter the password and then press the Enter key.  You should now have a terminal into your pi, in this particular case, via WiFi.


