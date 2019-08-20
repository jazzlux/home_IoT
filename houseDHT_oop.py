import paho.mqtt.client as mqtt
from database import Database

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("sensor/#")


#pomiary = {}
save_parameters = Database("oop.db")

def on_message(client, userdata, msg):
    message_topic= msg.topic
    message_payload = msg.payload
    print("%s %s" % (msg.topic, msg.payload))
    print(save_parameters.view_table())

    if message_topic == "sensor/temperature" :
        #temperature = float(message_payload)
        save_parameters.insert(temperature=float(message_payload))
    elif message_topic == "sensor/humidity":
        save_parameters.insert(humidity=float(message_payload))
    elif message_topic == "sensor/temp_inside":
        save_parameters.insert(temp_inside=float(message_payload))
    elif message_topic == "sensor/hum_inside":
        save_parameters.insert(hum_inside=float(message_payload))
    else:
        break


client = mqtt.Client()
#client.username_pw_set("dvukmvfa","JpfjsyzaE7Le")
client.on_connect = on_connect
client.on_message = on_message

def on_receive():
    client.subscribe()


def publish(topic, payload=None, qos=0, retain=False, hostname="localhost",
    port=1883, client_id="", keepalive=60, will=None, auth= {'username':"dvukmvfa", 'password':"JpfjsyzaE7Le"}, tls=None,
    protocol=mqtt.MQTTv311, transport="tcp"):

    client.publish("sensPy","1,1");
    print("publish")



client.connect("192.168.1.85", 1883, 60)
client.loop_forever()




#zeby latwo sie dodawalo funkcjonalnosc do backendu - wiecej relay's, wiecej sensorow etc
#sensor object - dodaje odczyt do database,
#relay object
