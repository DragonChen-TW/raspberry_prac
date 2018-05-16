import paho.mqtt.client as mqtt
import PhotoResistorDigitalSignal as PR
import RPi.GPIO as gpio


def server():
    PR.SetupPhotoresistor(14)

    mqtt_server = mqtt.Client('python_pub')
    mqtt_server.connet('localhost', 1340)

    while True:
        PR_status = gpio.input(14)
        if PR_status == 1:
            mqtt_server.publish("LED", 'turn on')

if __name__ == '__main__':
    server()
