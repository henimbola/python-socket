import socket


class ClientSocket:
    HEADER = 64
    PORT = 5050
    FORMAT = 'utf-8'
    DISCONNECT_MESSAGE = "!DISCONNECT"
    SERVER = socket.gethostbyname(socket.gethostname())
    client_socket = socket.socket()

    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        self.client_socket.connect((self.SERVER, self.PORT))
        self.send_message("Hello")

    def send_message(self, message):
        msg = message.encode(self.FORMAT)
        msg_length = len(msg)
        send_length = str(msg_length).encode(self.FORMAT)
        send_length += b' ' * (self.HEADER - len(send_length))

        self.client_socket.send(send_length)
        self.client_socket.send(msg)
        print(self.client_socket.recv(2048).decode(self.FORMAT))
