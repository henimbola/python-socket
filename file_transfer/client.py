import socket
import tqdm
import os

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096

host = '127.0.1.1'

port = 5001

file_name = "/home/henimbola/projects/sockets/DOC CV Jimmy Rakotobe.zip"
print(os.path.getsize(file_name))
file_size = os.path.getsize(file_name)

s = socket.socket()

print(f"[+] Connecting to {host}:{port}")
s.connect((host, port))
print(f"[+] Connected to {host}:{port}")

s.send(f"{file_name} {SEPARATOR} {file_size}".encode())

progress = tqdm.tqdm(range(file_size), f'Sending {file_name}', unit='B', unit_scale=True, unit_divisor=1024)
with open(file_name, "rb") as f:
    while True:
        # read the bytes from the file
        bytes_read = f.read(BUFFER_SIZE)
        if not bytes_read:
            # file transmitting is done
            break
        # we use sendall to assure transmission in
        # busy networks
        s.sendall(bytes_read)
        # update the progress bar
        progress.update(len(bytes_read))
# close the socket
s.close()
