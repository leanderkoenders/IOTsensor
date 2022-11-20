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
For the project I have decided to work with the ESP32 (see fig x), the reason behind it is because it has already Wi-Fi build in what is important for this project. The sensor I used for this project is a Ultrasonic Sensor HC-SR04 (see fig x). I also have a LED-display but it doesn´t add any value to my project, I just wanted to learn how to set that up (see fig x)

> Example:
>| IoT device | From this website         | Price |
>| --------- | ---------------- | -----------|
>| ESP32     | [Amazon](https://www.amazon.se/AZDelivery-ESP32-NodeMCU-Development-Efterf%C3%B6ljarmodul/dp/B07Z83MF5W/ref=asc_df_B07Z83MF5W/?tag=shpngadsglede-21&linkCode=df0&hvadid=476551177109&hvpos=&hvnetw=g&hvrand=11855222708416699519&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9062355&hvtargid=pla-898234157885&psc=1)    |  125 kr    |
>| Ultrasonic Sensor HC-SR04   |  [Elfa](https://www.elfa.se/en/hc-sr04-ultrasonic-distance-sensor-5v-adafruit-3942/p/30139186?ext_cid=shgooaqsesv-Shopping-PerformanceMax-CSS&&cq_src=google_ads&cq_cmp=18208288444&cq_con=&cq_term=&cq_med=pla&cq_plac=&cq_net=x&cq_pos=&cq_plt=gp&gclsrc=aw.ds&gclid=Cj0KCQiA99ybBhD9ARIsALvZavXpKyaKploFa4YCGR7lEYw9_48EFfpWBXGeCyqkvJlPmJfkQlxNtf4aAglyEALw_wcB&gclsrc=aw.ds)  |   50 kr     |
>| LED-display |[Amazon](https://www.amazon.se/ZHITING-seriell-LED-displaymodul-hallon-Arduino/dp/B08GM1XW31/ref=sr_1_41?crid=WQT82A1ZSX6F&keywords=lcd+oled+display&qid=1668767941&sprefix=lcd+oled+display%2Caps%2C72&sr=8-41)          |    40 kr |
> 

### Environment setup
I choose for Thonney IDE because I followed randromnerdtutorials to understand more about how to program EPS32 and they recommended Thonney IDE.  
I connect the EPS32 to the computer with a USB cable and after I write the code I can save it on the EPS32.
Here below are the steps you need to follow to set up every thing.
#### Installing
First step was to install Thonney 4.0.1. After that installation of Python, when that was finished I installed the lattest stable esptool.py with the comand prompt:

pip install esptool 

After that you also need to install the setuptools, there for you use command: 

pip install setuptools

At last one for this I filled in:

python -m esptool

#### MicroPython 
First download the MicroPython firmware (esp32-20220618-v1.19.1.bin). After the downloading you need to find the serial port number, in my case I didn’t saw a COM port available what meant that I didn’t had a USB driver so I needed to install CP210x Universal windows driver. 
Before the flashing the mircoPython firmware you need to erase the ESP32 flash memory. While holding down the boot button you need to runthe following command: 

python -m esptool –-chip esp32 erase_flash

When it was done you need to flash the MicroPython firmware to the ESP32. 
For the following step you need to replace in the code my port (COM4) with your own port. 
Then you need to hold down the boot butoon while you run the folling command:

python -m esptool --chip esp32 --port COM4 write_flash -z 0x1000 esp32-20220618-v1.19.1.bin

#### Tulip
Tulip is a software where you can make apps that companies use in the facotry think about work instructions, machine monitoring, takt time, ect. You need to have a licence to have access to the tulip enviroment. If you bought the licenence then you need to install the Tulip Player and run the following app: Sensor. 

### Putting everything together
 All the devices are connected in the following figure:
 
 ![screenshot of schema](https://user-images.githubusercontent.com/118463424/202922113-1a82c0b5-393e-4d4b-a421-85e87eba3f38.jpg)

Figure x
 
 The ESP32 is in the test set up powered by a powerbank. But because the powerbank had only a lifetime of 8 hours I decided that the device has to get the power supply of the workstation. This because otherwise someone is changing the battery every 8 hours and I wanted to have fixed instalation. The next plan is to scale from one sensor to 10 sensors at the workstation to see which of the positions need new material. Because there are a lot of pins not in use yet where we can connect sensors to. 
 
### Platforms and infrastructure
Like discribed earlier the company where I work for (Virtual manufacturing) wanted to connect the sensor to Tulip. Tulip is an software platform where you can build apps. In my case the sensor is connected to an app that gives a signal to the light tower on top of the workstation to turn red. All the data get stored in the tables of Tulip, this is in the cloud. 
The platform is cloud based and it is an paid subscription (if you want to have one license it cost about 24000 sek yearly). It is not suitable if you want to use the platform to connect it with the sensor because it is a lot of money. 
The intention of this project was focussed on replanishing the workstation with a signal so to look for an cheaper option I found the Blynk cloud platform. If the distance received from the sensor is bigger than x then Blynk can send out a signal to a mobile phone what can be carried by a warehouse employer.

### The code
When the ESP32 is connected to the power supply the first thing it does it connecting to the Wi-Fi with the folling code:
```
def connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        sta_if.active(True)
        sta_if.connect('network', 'password')
        while not sta_if.isconnected():
            pass # wait till connection
    print('network config:', sta_if.ifconfig())
    
connect()
```
After that it will go to the main.py where it imports all the liberys:
```
from machine import Pin, I2C
import ssd1306
from hcsr04 import HCSR04
from time import sleep
from umqtt.simple import MQTTClient
```
Then it will subscribe to the MQTT:
```
CLIENT_NAME = 'leander'
BROKER_ADDR = '172.16.2.7'
mqttc = MQTTClient(CLIENT_NAME, BROKER_ADDR, keepalive=60)
mqttc.connect()

#topic
BTN_TOPIC = 'Office/workstation/ONE/distance'
```
Then it will runs the rest of the code:
```
while True:
  oled.fill(0)
  
  #oled.show()
  distance = sensor.distance_mm()
  print('Distance:', (distance), 'mm')
  mqttc.publish( BTN_TOPIC, str(distance).encode() )
  if distance == -1:
      graph += "_"
  elif distance < 150:
      graph += "."
  else:
      graph += ":"
 
  last_chars = graph[-15:]
  print(graph)
  
  oled.text("Distance (mm)", 0, 15)
  oled.text(str(distance), 0, 35)
  oled.text(last_chars, 0, 55)
  oled.show()
  sleep(10)
  
  ```
  The distance gets measured and gets send to the MQTT and to the OLED display. On the OLED display is a small graph where if there is a fault value (-1) _ gets displayed and if the distance is between 0 and 150 there will be a . displayed. And if the distance is bigger then : will pop up on the display. 

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
 
 
  
