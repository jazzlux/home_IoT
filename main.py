from database import Database
from mqtt_connection import ConnToSensors
from plotting import Plotting

data = Database('newdb.db')
print(data.view_table())


#if __name__ == '__main__':

wykres = Plotting('newdb.db')
wykres.temp_hum() #plt.show() in plotting


    # def on_message(self, mqttc, obj, msg):
    #     self.dict_msg = []
    #     #print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))
    #     #print(self.database.view_table()
    #     self.dict_msg.append(msg.topic)
    #     self.dict_msg.append(msg.payload)
    #
    #     print(self.dict_msg)
