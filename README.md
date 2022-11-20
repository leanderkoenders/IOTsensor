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
>| IoT device | From this website         |
>| --------- | ---------------- |
>| ESP32     | xx          |
>| Ultrasonic Sensor HC-SR04   | xx |
>| 

### Environment setup
I choose for Thonney IDE because I followed randromnerdtutorials to understand more about how to program EPS32 and they recommended Thonney IDE.  
I connect the EPS32 to the computer with a USB cable and after I write the code I can save it on the EPS32.
Here below are the steps you need to follow to set up every thing.
#### Installing
First step was to install Thonney 4.0.1. After that installation of Python, when that was finished I installed the lastest stable esptool.py with the comand prompt: Pip install esptool 
After that you also need to install the setuptools, there for you use command: 
pip install setuptools
At last one for this I filled in:
python -m esptool
#### MicroPython 
First download the MicroPython firmware (esp32-20220618-v1.19.1.bin). After the downloading you need to find the serial port number, in my case I didn’t saw a COM port availbe what meant that I didn’t had a USB driver so I needed to install CP210x Universal windows driver. 
Before the flashing the mircoPython firmware you need to erase the ESP32 flash memory. While holding down the boot button you need to runthe following command: 
python -m esptool –-chip esp32 erase_flash.
When it was done you need to flash the MicroPython firmware to the ESP32. 
First you need to download 
While holding down the boot button I runned the following command:
python -m esptool --chip esp32 --port COM4 write_flash -z 0x1000 esp32-20220618-v1.19.1.bin




### Putting everything together
 Circuit diagram (can be hand drawn) (Fritzing, Tinkercad, etc.)
 Electrical calculations
 Limitations of hardware depending on design choices.
 Discussion about a way forward - is it possible to scale?
 
 
### Platforms and infrastructure
Describe your choice of platform(s). You need to describe how the IoT-platform works, and also the reasoning and motivation about your choices. Have you developed your own platform, or used

Is your platform based on a local installation or a cloud? Do you plan to use a paid subscription or a free? Describe the different alternatives on going forward if you want to scale your idea.

 Describe platform in terms of functionality
 Explain and elaborate what made you choose this platform
 Provide a pricing discussion. What are the prices for different platforms, and what are the pros and cons of using a low-code platform vs. developing yourself?
The code
Import core functions of your code here, and don't forget to explain what you have done. Do not put too much code here, focus on the core functionalities. Have you done a specific function that does a calculation, or are you using clever function for sending data on two networks? Or, are you checking if the value is reasonable etc. Explain what you have done, including the setup of the network, wireless, libraries and all that is needed to understand.

import this as that

def my_cool_function():
    print('not much here')

s.send(package)

# Explain your code!


### The physical network layer
How is the data transmitted to the internet or local server? Describe the package format. All the different steps that are needed in getting the data to your end-point. Explain both the code and choice of wireless protocols.

 How often is the data sent?
 Which wireless protocols did you use (WiFi, LoRa, etc ...)?
 Which transport protocols were used (MQTT, webhook, etc ...)
 Elaborate on the design choices regarding data transmission and wireless protocols. That is how your choices affect the device range and battery consumption.
 What alternatives did you evaluate?
 What are the design limitations of your choices?


### Visualisation and user interface
Describe the presentation part. How is the dashboard built? How long is the data preserved in the database?

 Provide visual examples on how the visualisation/UI looks. Pictures are needed.
 How often is data saved in the database. What are the design choices?
 Explain your choice of database. What kind of database. Motivate.
 Automation/triggers of the data.
 Alerting services. Are any used, what are the options and how are they in that case included.
Finalizing the design
Show the final results of your project. Give your final thoughts on how you think the project went. What could have been done in an other way, or even better? Pictures are nice!

 Show final results of the project
 Pictures
 *Video presentation

![image](https://user-images.githubusercontent.com/118463424/202917934-cea43ac0-efc6-45a3-82ef-af2057531f77.png)
