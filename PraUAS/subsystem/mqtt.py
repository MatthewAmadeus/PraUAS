import paho.mqtt.client as mqtt
from django.conf import settings

from .models import Sensor, SensorLog

def on_message_mqtt(sensor_name):
    def template(client, userdata, msg):
        sen = Sensor.objects.get(name=sensor_name)
        sen.value = msg.payload.decode('utf-8')
        sen.save()
        sen_log = SensorLog(name=sen, value=msg.payload.decode('utf-8'))
        sen_log.save()
    return template

def on_connect(client, userdata, rc, result):
    client.subscribe('1subsistem1/#')
    client.subscribe('1subsistem2/#')
    client.subscribe('1subsistem3/#')
    client.subscribe('2subsistem1/#')
    client.subscribe('2subsistem2/#')
    client.subscribe('2subsistem3/#')
    client.subscribe('3subsistem1/#')
    client.subscribe('3subsistem2/#')
    client.subscribe('3subsistem3/#')

on_message_sensor111 = on_message_mqtt('sensor111')
on_message_sensor112 = on_message_mqtt('sensor112')
on_message_sensor113 = on_message_mqtt('sensor113')

on_message_sensor121 = on_message_mqtt('sensor121')
on_message_sensor122 = on_message_mqtt('sensor122')
on_message_sensor123 = on_message_mqtt('sensor123')

on_message_sensor131 = on_message_mqtt('sensor131')
on_message_sensor132 = on_message_mqtt('sensor132')
on_message_sensor133 = on_message_mqtt('sensor133')

on_message_sensor211 = on_message_mqtt('sensor211')
on_message_sensor212 = on_message_mqtt('sensor212')
on_message_sensor213 = on_message_mqtt('sensor213')

on_message_sensor221 = on_message_mqtt('sensor221')
on_message_sensor222 = on_message_mqtt('sensor222')
on_message_sensor223 = on_message_mqtt('sensor223')

on_message_sensor231 = on_message_mqtt('sensor231')
on_message_sensor232 = on_message_mqtt('sensor232')
on_message_sensor233 = on_message_mqtt('sensor233')

on_message_sensor311 = on_message_mqtt('sensor311')
on_message_sensor312 = on_message_mqtt('sensor312')
on_message_sensor313 = on_message_mqtt('sensor313')

on_message_sensor321 = on_message_mqtt('sensor321')
on_message_sensor322 = on_message_mqtt('sensor322')
on_message_sensor323 = on_message_mqtt('sensor323')

on_message_sensor331 = on_message_mqtt('sensor331')
on_message_sensor332 = on_message_mqtt('sensor332')
on_message_sensor333 = on_message_mqtt('sensor333')


client = mqtt.Client()

client.message_callback_add('1subsistem1/sensor1', on_message_sensor111)
client.message_callback_add('1subsistem1/sensor2', on_message_sensor112)
client.message_callback_add('1subsistem1/sensor3', on_message_sensor113)

client.message_callback_add('1subsistem2/sensor1', on_message_sensor121)
client.message_callback_add('1subsistem2/sensor2', on_message_sensor122)
client.message_callback_add('1subsistem2/sensor3', on_message_sensor123)

client.message_callback_add('1subsistem3/sensor1', on_message_sensor131)
client.message_callback_add('1subsistem3/sensor2', on_message_sensor132)
client.message_callback_add('1subsistem3/sensor3', on_message_sensor133)

client.message_callback_add('2subsistem1/sensor1', on_message_sensor211)
client.message_callback_add('2subsistem1/sensor2', on_message_sensor212)
client.message_callback_add('2subsistem1/sensor3', on_message_sensor213)

client.message_callback_add('2subsistem2/sensor1', on_message_sensor221)
client.message_callback_add('2subsistem2/sensor2', on_message_sensor222)
client.message_callback_add('2subsistem2/sensor3', on_message_sensor223)

client.message_callback_add('2subsistem3/sensor1', on_message_sensor231)
client.message_callback_add('2subsistem3/sensor2', on_message_sensor232)
client.message_callback_add('2subsistem3/sensor3', on_message_sensor233)

client.message_callback_add('3subsistem1/sensor1', on_message_sensor311)
client.message_callback_add('3subsistem1/sensor2', on_message_sensor312)
client.message_callback_add('3subsistem1/sensor3', on_message_sensor313)

client.message_callback_add('3subsistem2/sensor1', on_message_sensor321)
client.message_callback_add('3subsistem2/sensor2', on_message_sensor322)
client.message_callback_add('3subsistem2/sensor3', on_message_sensor323)

client.message_callback_add('3subsistem3/sensor1', on_message_sensor331)
client.message_callback_add('3subsistem3/sensor2', on_message_sensor332)
client.message_callback_add('3subsistem3/sensor3', on_message_sensor333)


client.on_connect = on_connect

client.connect(settings.MQTT_HOST, settings.MQTT_PORT)
