# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()
# Complete project details at https://RandomNerdTutorials.com/micropython-hc-sr04-ultrasonic-esp32-esp8266/
from hcsr04 import HCSR04
from time import sleep


#wifi
def connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        sta_if.active(True)
        sta_if.connect('Virtual-GBG', 'awellhiddensecret')
        while not sta_if.isconnected():
            pass # wait till connection
    print('network config:', sta_if.ifconfig())
    
connect()

# ESP32
sensor = HCSR04(trigger_pin=5, echo_pin=18, echo_timeout_us=10000)

# ESP8266
#sensor = HCSR04(trigger_pin=12, echo_pin=14, echo_timeout_us=10000)

'''while True:
    distance = sensor.distance_cm()
    "print('Distance:', distance, 'cm')"
    sleep(1)'''