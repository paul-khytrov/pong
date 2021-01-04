import socket
import json
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.1.42', 10082))             #тут айпішкі якісь свої впишеш
s.listen(100)
conn, addr = s.accept()
print("connected:", addr)
while True:
    data = conn.recv(10000)
    rdata = json.loads(data.decode())
    print(rdata)
    data = ''
    rdata = [0, 0]
