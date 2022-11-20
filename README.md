# IOTsensor
Sensor for IOT

IOT sensor to replanish the workstation

Writer of the report: Leander Koenders


### Project overview
The goal of the course was to see if it was possible to connect a sensor to Tulip (a software platform, later in the report it will be highlighted). With this report it would be possible to set up everything within 6-8 hours (plus one day of learning the platform Tulip where the sensor is connected to)


### Objectives
At my company (virtual) there was a need to see if a workstation needed to be refilled or not. We also wanted to see if the positions at the workstation where empty by sensors rather then by a human that was scanning a bucket. And the best way to do this was to have a sensor detecting if there is a bucket there or not. So the sensor measures the distance to the bucket and if the distance is bigger then it means that the bucket is not any more at its place. Then there will be a signal sended out that the workstation needs to be replanished. 
With this project I want to give customers of us the option of having a workstation that can give a signal to the warehouse that it needs materials without the operator having to do something. 

### Material
For the project I have decided to work with the ESP32 (see fig x) , the reason behind it is because it has already Wi-Fi build in what is important for this project. The sensor I used for this project is a Ultrasonic Sensor HC-SR04 (see fig x).  

> Example:
>| IoT Thing | For this         |
>| --------- | ---------------- |
>| ESP32     | a table          |
>| Ultrasonic Sensor HC-SR04   | jolly good idea? |
>| 

### Environment setup
I choose for Thonney IDE because I followed randromnerdtutorials to understand more about how to program EPS32 and they recommended Thonney IDE.  
I connect the EPS32 to the computer with a USB cable and after I write the code I can save it on the EPS32.


Steps that you needed to do for your computer. Instalation of drivers, etc. 
First step was to install Thonney 4.0.1. After that installation of Python, when that was finished I installed the lastest stable esptool.py with pip. 
Pip install esptool 
I also needed to install the setuptools: pip install setuptools
At last one for this I filled in python -m esptool
Then I downloaded the MicroPython firmware (esp32-20220618-v1.19.1.bin). After the downloading I needed to find the serial port number but I didn’t saw a COM port availbe what meant that I didn’t had a USB driver so I needed to install CP210x Universal windows driver. 
Before the flashing the mircoPython firmware I needed to erase the ESP32 flash memory. While holding down the boot button. I runned the following command: python -m esptool –-chip esp32 erase_flash. When it was done -> flashing MicroPython firmware to the ESP32. 
While holding down the boot button I runned the following command:  python -m esptool --chip esp32 --port COM4 write_flash -z 0x1000 esp32-20220618-v1.19.1.bin

