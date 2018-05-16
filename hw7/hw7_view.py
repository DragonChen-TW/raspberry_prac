import paho.mqtt.client as mqtt
import PIR, time, socket
import RPi.GPIO as gpio

def onConnect(view, data, flags, rc):
    print('Connected with result code {}'.format(rc))
    view.subscribe('goods')
def onMessage(view, data, msg):
    print(msg.topic, msg.payload)
    # uni_str = str(msg.payload, 'utf-8')
    global send_msg
    send_msg = msg.payload

def mqttSetup():
    global view
    view = mqtt.Client()
    view.on_connect = onConnect
    view.on_message = onMessage
    view.connect('localhost', 1883, 60)
    # force to start connect
    view.loop_start()
def mqttSend():
    global view
    view.publish('request', 'request')

def listen():
    global view
    PIR.setup(14)
    while not gpio.input(14):
        time.sleep(1)
    print('PIR detected!')

def server():
    global send_msg
    bind_ip = '192.168.1.18'
    bind_port = 8888

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((bind_ip, bind_port))
    server_socket.listen(5)

    try:
        print('Listening on {}'.format((bind_ip, bind_port)))
        conn_socket, addr = server_socket.accept()
        print('Accept connection from {}'.format((addr[0], addr[1])))

        conn_socket.send(send_msg)
    finally:
        server_socket.close()
        conn_socket.close()

if __name__ == '__main__':
    try:
        mqttSetup()
        listen()
        mqttSend()

        server()
    finally:
        PIR.clean()
