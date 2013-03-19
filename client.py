import socket   #for sockets
import sys  #for exit
#import pygame
from thread  import *
from codex import *
from decode import *
from encode import *

users = []
self_id = -1
byteRec = 1024
tmpCode = ""

#Set initial name and code variables (unique to each user)
userName = raw_input("Username: ")
global codex
codex = str(raw_input("Enter the codex: "))

#Deals with incoming messages
def parse(data):
	#Pulls variable self_id from outside the function
    global self_id
	
	#splits message, taking the first element (assignment type) and the message as seperate variables
    cmd = data[0]
    msg = data[1:]
	
	# [server based identifier?]
    if cmd == 'c':
        self_id = int(msg)
	#Checks to see who owns the message, each message sent is attributed a identifier: 't'
    elif cmd == 't':
        params = msg.split(',',1)
        id = int(params[0])
		#If the association id does not match the users print the message
        if id != self_id:
			decode(params[1])
			print tmpCode

def serverlisten(socket):
    
    while True:
        data = socket.recv(byteRec)
        if not data:
            break
        cmds = data.split(';')
        for i in cmds:
            if i:
                parse(i)

ip   = raw_input("Server ip: ");
port = input("Server port: ");
try:
    #create an AF_INET, STREAM socket (TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    sys.exit()

print 'Socket Created'
s.connect((ip,port))
start_new_thread(serverlisten ,(s,))
while 1:
	#User generation of their message 
	#Input of code? Possible automation when linked to server)
	def message():
		raw = str(raw_input("Input message here: "))
		print ""
		temp = raw.lower()
		phrase = list(temp)
		CodeCreate(phrase)
	
	message()
	msg = "["+userName+"]" + " " + tmpCode
	msg.replace(';','')
	s.send("t"+msg)

s.close()