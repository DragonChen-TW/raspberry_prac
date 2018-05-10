import RPi.GPIO as gpio
import socket, LED

def server():
    bind_ip = '192.168.10.33'
    bind_port = 8888

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((bind_ip, bind_port))
    server_socket.listen(5)

    print('Listening on {}'.format((bind_ip, bind_port)))

    gpio.setmode(gpio.BCM)
    LED.setup(21, 'out')

    try:
        conn_socket, addr = server_socket.accept()
        print('Accept connection from {}'.format((addr[0], addr[1])))
        while True:
            data = conn_socket.recv(1024)
            data = str(data, 'utf-8')
            if data == 'turn on':
                LED.turnON(21)
            elif data == 'turn off':
                LED.turnOFF(21)
    finally:
        server_socket.close()
        conn_socket.close()
        gpio.cleanup()

if __name__ == '__main__':
    server()
