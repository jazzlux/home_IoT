import paho.mqtt.client as mqtt
from database import Database
import os
import time


payload = 0
hum = 0
temp_inside = 0
hum_inside = 0


class ConnToSensors(mqtt.Client):


    def __init__(self, server, port, database_name, user="", password=""):
        super().__init__()
        self.server = server
        self.port = port
        self.user = user
        self.password = password
        self.database = Database(database_name)



    def on_connect(self, mqttc, obj, flags, rc):
        print("rc: "+str(rc))

    def on_subscribe(self, mqttc, obj, mid, granted_qos):
        print("Subscribed: "+str(mid)+" "+str(granted_qos))



    def on_message(self, mqttc, obj, msg):
        global payload
        global hum
        global temp_inside
        global hum_inside
        #print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))
        #print(self.database.view_table())

        topic = os.path.basename(msg.topic)
        print(topic)
        #print(topic,  msg.payload)

        if topic == "temperature" :
            payload = msg.payload.decode('utf-8')
            # print("to database?")
            self.database.insert(temperature = float(msg.payload))
        elif topic == "humidity":
            hum = msg.payload.decode('utf-8')
            self.database.insert(humidity = float(msg.payload))
        elif topic == "temp_inside":
            temp_inside = msg.payload.decode('utf-8')
            self.database.insert(temp_inside = float(msg.payload))
            self.database.close()
        elif topic == "hum_inside":
            hum_inside = msg.payload.decode('utf-8')
            self.database.insert(hum_inside = float(msg.payload))
            self.database.close()

    def run_sub(self, sub_topic):
        self.username_pw_set(self.user, self.password)
        self.connect(self.server, self.port, 60)
        self.subscribe(sub_topic, 1)
        #print('subscribed this')
        self.loop_start()
        # rc = 0
        # while rc == 0:
        #     rc = self.loop()
        #print("pp")
        # self.loop_stop()

        #return rc

    # def run_sub(self, sub_topic):
    #     self.username_pw_set(self.user, self.password)
    #     self.connect(self.server, self.port, 60)
    #     self.subscribe(sub_topic, 1)
    #     print('subscribed this')
    #     # self.loop_start()
    #     rc = 0
    #     while rc == 0:
    #         rc = self.loop()
    #     #print("pp")
    #     # self.loop_stop()
    #
    #     return rc


if __name__ == '__main__':
    # mqttc = ConnToSensors("m24.cloudmqtt.com", 17208, "newdb.db", "dvukmvfa","JpfjsyzaE7Le")
    # rc = mqttc.run_sub("sensors/#")
    d = Database("newdb.db")
    print(d.view_table())
