import paho.mqtt.client as mqtt
import PIR
import RPi.GPIO as gpio

def server():
    mqtt_server = mqtt.Client('python_pub')
    mqtt_server.connect('localhost', 1883)

    while True:
        PR_status = gpio.input(14)
        if PR_status == 1:
            mqtt_server.publish("LED", 'turn on')

if __name__ == '__main__':
    try:
        PIR.setup(14)
        server()
    finally:
        PIR.clean()
