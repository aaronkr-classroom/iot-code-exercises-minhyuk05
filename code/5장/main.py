#main.py

from device inport SensorDevice, ActuatorDevice, TemperatureSensor, LightSensor

sensor = SensorDevice("Temp Sensor")
actuator = ActuatorDevice("LED Controller")

sensor.connect()
actuator.connect()

print(sensor.status())
print(actuator.status())
print()

temp = TemperatureSensor("Temp1")
light = LightSensor("Light1")

print("Temp: ", temp.read())
print("Light: ", light.read())
