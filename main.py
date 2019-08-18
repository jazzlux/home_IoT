from sensors import ConnToSensors

mqttc = ConnToSensors()

rc = mqttc.run_sub()
print("rc: "+str(rc))
