import paho.mqtt.client as mqtt
import LED

def on_connect(client, data, flags, rc):
    print('Connected with result code {}'.format(rc))
    client.subscribe("LED")

def on_message(client, data, msg):
    print(msg.topic, msg.payload)
    if msg.payload == b'turn on':
        LED.turnON(21)

def client():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect('localhost', 1340, 60)
    client.loop_forever()

if __name__ == '__main__':
    try:
        LED.setup(21, 'out')
        client()
    except:
        LED.clean()
