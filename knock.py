import socket
import sys

def Knock(host,port):
	print("Knocking", host+":"+str(port));
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(0.1)
	try:
		s.connect((host,port))
	except socket.timeout:
		s.close()
		return
	s.shutdown(socket.SHUT_RDWR)
	s.close()

if (len(sys.argv)<3):
	print("Use: knock.py host port [port]...")
	exit(0)

#print("args:",str(sys.argv))

host = sys.argv[1]
for i in range(2,len(sys.argv)):
	Knock(host, int(sys.argv[i]))