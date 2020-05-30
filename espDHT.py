from umqtt.simple import MQTTClient
from machine import Pin
import machine
import micropython
import time
#import gc
#import os
import network
import dht

blue_led = Pin(2, Pin.OUT, value=1)
led = Pin(4, Pin.OUT, value=1)
online_led = Pin(5, Pin.OUT)

# SERVER = ""
SERVER = "192.168.1.85"
CLIENT_ID = 'ESP' #sprawdzic czy to ma znaczenie (duze/male litery)
PORT = 1883
# PORT =
# USER = ""
# PASSWORD = ""
TOPIC = b"sensor"


def do_connect():

    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('ADSLPT-TR2355FF', '4B781E8D0B')
        # print(sta_if.status())
        while not sta_if.isconnected():
            pass
    # print('network config:', sta_if.ifconfig())
    if sta_if.status() == 5:
        return True
    else:
        return False




def do_disconnect():
    net_module = network.WLAN(network.STA_IF)
    if net_module.isconnected():
        net_module.disconnect()
        if net_module.status() == 0:
            print("disconnected from network")


def blue_led_blink(num):
    for item in range(0,num):
        blue_led.value(0)
        time.sleep(0.05)
        blue_led.value(1)
        time.sleep(0.05)


sensor = dht.DHT22(Pin(12))

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
          print(msg)
          return(msg)

        else:
            return('Invalid sensor readings.')
    except OSError as e:
      return('Failed to read sensor.')


# do_connect()
#dht_readings()


def mqtt_publish(first_msg, second_msg):
    # c = MQTTClient(CLIENT_ID, SERVER, PORT, USER, PASSWORD, keepalive=0)
    c = MQTTClient(CLIENT_ID, SERVER, PORT, keepalive=0)

    c.connect()
    c.publish(b'sensors/temperature', (b'{0:3.1f}'.format(first_msg)))
    c.publish(b'sensors/humidity', (b'{0:3.1f}' .format(second_msg)))
    blue_led_blink(4)
    c.disconnect()


def main(period):
    while True:
        if do_connect() == True:
            dht_readings()
            mqtt_publish(temp,hum)
            do_disconnect()
        else:
            print("can't connect to network right now")
            time.sleep(60)
        time.sleep(period)


main(300)
