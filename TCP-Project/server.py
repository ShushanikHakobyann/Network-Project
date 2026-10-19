import socket

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("10.0.0.2", 5000))
server.listen(1)

print("Server is waiting for a file....")

conn, addr=server.accept()
print("Connected by:", addr)

with open("/tmp/received.txt", "wb") as f:
    while True:
        data=conn.recv(1024)
        if not data:
            break
        f.write(data)

print("File received successfully!")

conn.close()
server.close()
