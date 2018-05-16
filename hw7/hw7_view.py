import paho.mqtt.client as mqtt
import PIR, time
import RPi.GPIO as gpio

def onConnect(view, data, flags, rc):
    print('Connected with result code {}'.format(rc))
    view.subscribe('goods')
def onMessage(view, data, msg):
    print(msg.topic, msg.payload)

def mqttSetup():
    global view
    view = mqtt.Client()
    view.on_connect = onConnect
    view.on_message = onMessage
    view.connect('localhost', 1883, 60)
def mqttSend():
    global view
    view.publish('request', 'request')
def mqttLoop():
    global view
    view.loop_forever()

def listen():
    global view
    PIR.setup(14)
    while not gpio.input(14):
        time.sleep(1)
    print('PIR detected!')

if __name__ == '__main__':
    try:
        mqttSetup()
        listen()
        mqttSend()
        mqttLoop()
    finally:
        PIR.clean()
