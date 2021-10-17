import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = socket.gethostbyname('1-ne01.bootupctf.com')
port = 7090

s.connect(ip, port)

print(s.recv(1024).decode)