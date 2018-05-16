import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time

TopicServerIP = "192.168.1.18"
TopicServerPort = 1883
TopicName = "PIR"
counter = 0
mqttc = mqtt.Client("python_pub")
mqttc.connect(TopicServerIP,TopicServerPort)

def setup(GPIOnum):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIOnum, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

def motion(GPIOnum):
    global counter
    if GPIO.input(GPIOnum):
        counter += 1
        print("Motion detected{0}".format(counter))
        mqttc.publish(TopicName, "milktea for sale")

    else:
        print("Motion not detected")

if __name__ == "__main__":
    setup(14)
try:
    GPIO.add_event_detect(14, GPIO.BOTH, callback = motion, bouncetime = 500)
    while True:
        time.sleep(1)

except :
    GPIO.cleanup()
