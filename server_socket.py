import socket
import threading
import os


class ServerSocket:
    SERVER_HOST = socket.gethostbyname(socket.gethostname())
    SERVER_SOCKET = socket.socket()
    HEADER = 64
    PORT = 5050
    FORMAT = 'utf-8'
    DISCONNECT_MESSAGE = '!DISCONNECT'

    def __init__(self):
        self.SERVER_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.SERVER_SOCKET.bind((self.SERVER_HOST, self.PORT))

    def start(self):
        print('[STARTING] The server is starting...')
        self.SERVER_SOCKET.listen()
        print(f'[LISTENING] Server is listening on {self.SERVER_HOST}')
        while True:
            conn, address = self.SERVER_SOCKET.accept()
            thread = threading.Thread(target=self.handle_client, args=(conn, address))
            thread.start()
            print(f'[ACTIVE CONNECTIONS] {threading.activeCount() - 1}')

    def handle_client(self, conn, address):
        print(f'[NEW CONNECTED] {address} connected')

        connected = True
        while connected:
            msg_length = conn.recv(self.HEADER).decode(self.FORMAT)
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(self.FORMAT)

                if msg == self.DISCONNECT_MESSAGE:
                    connected = False

                if msg == "code":
                    os.system('code .')

                print(f'[{address}] {msg}')
                conn.send(input().encode(self.FORMAT))

            else:
                print(f'[{address}] No Message')
                connected = False

        conn.close()
