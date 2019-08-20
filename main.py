from sensors import ConnToSensors

mqttc = ConnToSensors("m24.cloudmqtt.com", 17208, "newdb.db", "dvukmvfa","JpfjsyzaE7Le")

rc = mqttc.run_sub("sensors/#")
print(mqttc.on_message())
