import socket

def client():
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('192.168.10.33', 8888))

        while True:
            data = input()
            data = data.encode()
            client_socket.send(data)
    finally:
        client_socket.close()

if __name__ == '__main__':
    client()
