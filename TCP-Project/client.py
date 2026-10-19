import socket 

client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("10.0.0.2", 5000))

with open("/tmp/message.txt", "rb") as f:
    while True:
        data=f.read(1024)
        if not data:
            break
        client.sendall(data)

client.close()
print("File sent succesfully!")

