import paho.mqtt.client as mqtt
from database import Database



class ConnToSensors(mqtt.Client):
    database = Database("newdb.db")

    # def on_connect(self, mqttc, obj, flags, rc):
    #     print("rc: "+str(rc))

    def on_message(self, mqttc, obj, msg):
        print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))


    # def on_publish(self, mqttc, obj, mid):
    #     print("mid: "+str(mid))

    # def on_subscribe(self, mqttc, obj, mid, granted_qos):
    #     print("Subscribed: "+str(mid)+" "+str(granted_qos))

    # def quick_pub(self, topic, message):
    #     self.username_pw_set("dvukmvfa","JpfjsyzaE7Le")
    #     self.connect("m24.cloudmqtt.com", 17208, 60)
    #     self.publish(topic, message)

    def run_sub(self, user, password):
        self.username_pw_set(user, password)
        self.connect("m24.cloudmqtt.com", 17208, 60)
        self.subscribe("swiatlo", 1)

        rc = 0
        while rc == 0:
            rc = self.loop()
        return rc





mqttc = ConnToSensors()

rc = mqttc.run_sub("dvukmvfa","JpfjsyzaE7Le")
print("rc: "+str(rc))



#database
#ploting?
#mqtt
