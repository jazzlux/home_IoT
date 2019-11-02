from umqtt.simple import MQTTClient
from machine import Pin
import machine
import micropython
import time
#import gc
#import os
import network
import dht

blue_led = Pin(2, Pin.OUT, value=0)
led = Pin(4, Pin.OUT, value=0)
online_led = Pin(5, Pin.OUT)

SERVER = "m24.cloudmqtt.com"
CLIENT_ID = 'ESP' #sprawdzic czy to ma znaczenie (duze/male litery)
PORT = 17208
USER = "dvukmvfa"
PASSWORD = "JpfjsyzaE7Le"
TOPIC = b"sensor"



def do_connect():

    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('ADSLPT-TR2355FF', '4B781E8D0B')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())




def blue_led_blink(num):
    for item in range(0,num):
        blue_led.value(1)
        time.sleep(0.05)
        blue_led.value(0)
        time.sleep(0.05)



#do_connect()

sensor = dht.DHT22(Pin(18))

def dht_readings():
    global temp, hum
    try:
        sensor.measure()
        temp_tag = b"temperature"
        hum_tag = "humidity"
        temp = sensor.temperature()
        hum = sensor.humidity()
        if (isinstance(temp, float) and isinstance(hum, float)) or (isinstance(temp, int) and isinstance(hum, int)):
          msg = (b'{0:3.1f},{1}'.format(temp, hum))
          hum = round(hum, 2)
          return(msg)

        else:
            return('Invalid sensor readings.')
    except OSError as e:
      return('Failed to read sensor.')




do_connect()


def mqtt_publish():
    c = MQTTClient(CLIENT_ID, SERVER, PORT, USER, PASSWORD, keepalive=0)
    c.connect()
    c.publish(b'sensors/temperature', (b'{0:3.1f}'.format(temp)))
    c.publish(b'sensors/humidity', (b'{0:3.1f}' .format(hum)))
    blue_led_blink(4)
    c.disconnect()


def main(period):
    while True:
        dht_readings()
    
        mqtt_publish()
        time.sleep(period)

main(15)
