import socket
import tqdm
import os
import tkinter as tk

root = tk.Tk()

canvas1 = tk.Canvas(root, width=300, height=300)
canvas1.pack()


def hello():

    print('test')

    # label1 = tk.Label(root, text='Hello World!', fg='green', font=('helvetica', 12, 'bold'))
    # canvas1.create_window(150, 200, window=label1)

    SERVER_HOST = socket.gethostbyname(socket.gethostname())
    SERVER_PORT = 5001
    BUFFER_SIZE = 4096
    SEPARATOR = "<SEPARATOR>"

    s = socket.socket()
    s.bind((SERVER_HOST, SERVER_PORT))

    s.listen(5)
    print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")

    conn, address = s.accept()
    print(f'[+] {address} is connected')

    # receive the file infos
    # receive using client socket, not server socket
    received = conn.recv(BUFFER_SIZE).decode()
    file_name, file_size = received.split(SEPARATOR)
    # remove absolute path if there is
    file_name = os.path.basename(file_name)
    # convert to integer
    file_size = int(file_size)

    # start receiving the file from the socket
    # and writing to the file stream
    progress = tqdm.tqdm(range(file_size), f"Receiving {file_name}", unit="B", unit_scale=True, unit_divisor=1024)
    with open(file_name, "wb") as f:
        while True:
            # read 1024 bytes from the socket (receive)
            bytes_read = conn.recv(BUFFER_SIZE)
            if not bytes_read:
                # nothing is received
                # file transmitting is done
                break
            # write to the file the bytes we just received
            f.write(bytes_read)
            # update the progress bar
            progress.update(len(bytes_read))

    # close the client socket
    conn.close()
    # close the server socket
    s.close()


button1 = tk.Button(text='Listen to transfer', command=hello, bg='brown', fg='white')
canvas1.create_window(150, 150, window=button1)

root.mainloop()
