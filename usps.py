import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
port = 4444
flag = open("flag.py")
s.bind((host,port))
s.listen(5)
while True:
	clientSocket, addr = s.accept()
	print("gotem on %s % str(addr))
	clientSocket.send(flag.read())
flag.close()
clientSocket.close()
