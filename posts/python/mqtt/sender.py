"""
Enviando json para o broker

Lib para fazer a conexão com mqtt:
'''
    pip install paho-mqtt
'''
"""
import json
import paho.mqtt.client as mqtt

#Connection success callback
def on_connect(client, userdata, flags, rc):
    print('connectado')

client = mqtt.Client()

# Specify callback function
client.on_connect = on_connect

# Establish a connection
client.connect('localhost', 1883, 60)
client.publish('hello', payload=json.dumps({"msg": "Blz"}), qos=0)
