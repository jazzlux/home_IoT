from database import Database
from mqtt_connection import ConnToSensors
from plotting import Plotting

data = Database('newdb.db')
print(data.view_table())

#dd = ConnToSensors("m24.cloudmqtt.com", 17208, "newdb.db", "dvukmvfa","JpfjsyzaE7Le")
#rc = dd.run_sub("sensors/#")
#if __name__ == '__main__':

wykres = Plotting('newdb.db')
wykres.temp_hum()



    # def on_message(self, mqttc, obj, msg):
    #     self.dict_msg = []
    #     #print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))
    #     #print(self.database.view_table()
    #     self.dict_msg.append(msg.topic)
    #     self.dict_msg.append(msg.payload)
    #
    #     print(self.dict_msg)









# mqttc = ConnToSensors("m24.cloudmqtt.com", 17208, "newdb.db", "dvukmvfa","JpfjsyzaE7Le")
# #mqtt_connect = testCls("m24.cloudmqtt.com", 17208, "newdb.db", "dvukmvfa","JpfjsyzaE7Le")
# #rc = mqttc.run_sub("sensors/#")
#
# mqttc.message_callback_add("sensors/temperature", mqttc.on_message_msgs)
# mqttc.message_callback_add("sensors/hum_inside", mqttc.on_message_bytes)
# mqttc.run_sub("sensors/#")
#
#
# mqttc2 = ConnToSensors("m24.cloudmqtt.com", 17208, "newdb.db", "dvukmvfa","JpfjsyzaE7Le")
# mqttc2.message_callback_add("sensors/te", mqttc2.on_message_msgs)
# mqttc2.message_callback_add("sensors/hu", mqttc2.on_message_bytes)
# mqttc2.run_sub("sensors/#")



# mqtt_connect2 = testCls2("m24.cloudmqtt.com", 17208, "newdb.db", "dvukmvfa","JpfjsyzaE7Le")
# rc2 = mqtt_connect2.run_sub("sensors/hum_inside")
