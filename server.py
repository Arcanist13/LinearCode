import socket
import sys
#from objects import *
from thread import *

class User:
    colour = 'white'
    x      = 0
    y      = 0
    id     = -1

user_count = 0
connections = []
 
HOST = ''   # Symbolic name meaning all available interfaces
PORT = 8888 # Arbitrary non-privileged port
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print ("Socket created")
 
#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ', Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'
 
#Start listening on socket
s.listen(8)
print 'Socket now listening'
 
#Function for handeling the messages sent from users
def parse(data,user):
    cmd = data[0]
    msg = data[1:]
	
	#
    if cmd == 't':
        print msg
		#Sends message to other connected users, with senders.id attatched
        broadcast("t"+str(user.id)+","+msg)
	#
    elif cmd == 'm':
        params = msg.split(',')
        if params >= 2:
            user.x += int(params[0])
            user.y += int(params[1])
        broadcast("m"+str(user.id)+","+params[0]+","+params[1])

def broadcast(data):
    global connections
    data = data+';'
    for i in connections:
        i.sendall(data)

#Function for handling connections. This will be used to create threads
#Handles when a user connects to the server
def clientthread(conn):
    global user_count
    global colours
    user = User()
    user.id = user_count
    user_count += 1
    conn.sendall("c"+str(user.id))
	#Must have user.id attatched to send to other users (not return to original)
    broadcast("a"+str(user.id)+","+str(user.x)+","+str(user.y))
     
    #infinite loop so that function do not terminate and thread do not end.
    while True:
         
        #Receiving from client
        data = conn.recv(1024)
        if not data:
            break
        cmds = data.split(';')
        for i in cmds:
            parse(i,user)
     
    #came out of loop
    conn.close()
 
#now keep talking with the client
while True:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    print 'New user connected with ' + addr[0] + ':' + str(addr[1])
     
    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    connections.append(conn)
    start_new_thread(clientthread ,(conn,))
 
s.close()