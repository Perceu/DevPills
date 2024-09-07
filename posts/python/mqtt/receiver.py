"""
Client para recebendo mensagens no terminal

Lib para fazer a conexão com mqtt:
'''
    pip install paho-mqtt
'''
"""
import paho.mqtt.client as mqtt

#Connection success callback
def on_connect(client, userdata, flags, rc):
    print('Connected with result code '+str(rc))
    client.subscribe('hello/#')

# Message receiving callback
def on_message(client, userdata, msg):
    print(msg.payload)

client = mqtt.Client()

# Specify callback function
client.on_connect = on_connect
client.on_message = on_message

# Establish a connection
client.connect('localhost', 1883, 60)
client.loop_forever()