import paho.mqtt.client as mqtt
from database import Database



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
        self.dict_msg = []
        #print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))
        #print(self.database.view_table()
        self.dict_msg.append(msg.topic)
        self.dict_msg.append(msg.payload)

        return self.dict_msg

        #self.database.insert(str(msg.topic)=float(msg.payload))


    def run_sub(self, sub_topic):
        self.username_pw_set(self.user, self.password)
        self.connect(self.server, self.port, 60)
        #self.loop()
        self.subscribe(sub_topic, 1)

        rc = 0
        while rc == 0:
            rc = self.loop()
        return rc






# mqttc = ConnToSensors("m24.cloudmqtt.com", 17208, "newdb.db", "dvukmvfa","JpfjsyzaE7Le")
#
# rc = mqttc.run_sub("sensors/#")




#database
#ploting?
#mqtt
