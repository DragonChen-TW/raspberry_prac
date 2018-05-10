import socket

def client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect('')

if __name__ == '__main__':
    client()
