import socket   #for sockets
import sys  #for exit
#import pygame
from thread  import *
from codex import *

users = []
self_id = -1
byteRec = 1024

#Set initial name and code variables (unique to each user)
userName = raw_input("Username: ")
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
			def CodeCovert():
				#Apply linear translation based on codex (reverse)
				def linearTran(msg):
					for i in range(len(msg)):
						msg[i] = (msg[i]+(32-(tran)))%32
						if msg[i] == 0:
							msg[i] = 32
					numCode = msg
					codedMsg(numCode)

				#Convert numeric representation to text
				def codedMsg(msg):
					for i in range(len(msg)):
						if msg[i] == 1:
							msg[i] = 'a'
						elif msg[i] == 2:
							msg[i] = 'b'
						elif msg[i] == 3:
							msg[i] = 'c'
						elif msg[i] == 4:
							msg[i] = 'd'
						elif msg[i] == 5:
							msg[i] = 'e'
						elif msg[i] == 6:
							msg[i] = 'f'
						elif msg[i] == 7:
							msg[i] = 'g'
						elif msg[i] == 8:
							msg[i] = 'h'
						elif msg[i] == 9:
							msg[i] = 'i'
						elif msg[i] == 10:
							msg[i] = 'j'
						elif msg[i] == 11:
							msg[i] = 'k'
						elif msg[i] == 12:
							msg[i] = 'l'
						elif msg[i] == 13:
							msg[i] = 'm'
						elif msg[i] == 14:
							msg[i] = 'n'
						elif msg[i] == 15:
							msg[i] = 'o'
						elif msg[i] == 16:
							msg[i] = 'p'
						elif msg[i] == 17:
							msg[i] = 'q'
						elif msg[i] == 18:
							msg[i] = 'r'
						elif msg[i] == 19:
							msg[i] = 's'
						elif msg[i] == 20:
							msg[i] = 't'
						elif msg[i] == 21:
							msg[i] = 'u'
						elif msg[i] == 22:
							msg[i] = 'v'
						elif msg[i] == 23:
							msg[i] = 'w'
						elif msg[i] == 24:
							msg[i] = 'x'
						elif msg[i] == 25:
							msg[i] = 'y'
						elif msg[i] == 26:
							msg[i] = 'z'
						elif msg[i] == 27:
							msg[i] = '!'
						elif msg[i] == 28:
							msg[i] = '.'
						elif msg[i] == 29:
							msg[i] = ','
						elif msg[i] == 30:
							msg[i] = '?'
						elif msg[i] == 31:
							msg[i] = '"'
						elif msg[i] == 32:
							msg[i] = " "
						else:
							print "Invalid syntax. " + "\'" + str(msg[i]) + "\'" + "is not defined."
							message()
					codeMsg = msg
					tmpCode = ""
					for i in range(len(codeMsg)):
						tmpCode = str(tmpCode) + str(codeMsg[i])
					return tmpCode
				
				linearTran(params[1])

			CodeConvert()
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
	def CodeCreate():
		#User generation of their message 
		#Input of code? Possible automation when linked to server)
		def message():
			raw = str(raw_input("Input message here: "))
			print ""
			temp = raw.lower()
			phrase = list(temp)
			encode(phrase)

		#Translate text to numeric
		def encode(msg):
			for i in range(len(msg)):
				if msg[i] == 'a':
					msg[i] = 1
				elif msg[i] == 'b':
					msg[i] = 2
				elif msg[i] == 'c':
					msg[i] = 3
				elif msg[i] == 'd':
					msg[i] = 4
				elif msg[i] == 'e':
					msg[i] = 5
				elif msg[i] == 'f':
					msg[i] = 6
				elif msg[i] == 'g':
					msg[i] = 7
				elif msg[i] == 'h':
					msg[i] = 8
				elif msg[i] == 'i':
					msg[i] = 9
				elif msg[i] == 'j':
					msg[i] = 10
				elif msg[i] == 'k':
					msg[i] = 11
				elif msg[i] == 'l':
					msg[i] = 12
				elif msg[i] == 'm':
					msg[i] = 13
				elif msg[i] == 'n':
					msg[i] = 14
				elif msg[i] == 'o':
					msg[i] = 15
				elif msg[i] == 'p':
					msg[i] = 16
				elif msg[i] == 'q':
					msg[i] = 17
				elif msg[i] == 'r':
					msg[i] = 18
				elif msg[i] == 's':
					msg[i] = 19
				elif msg[i] == 't':
					msg[i] = 20
				elif msg[i] == 'u':
					msg[i] = 21
				elif msg[i] == 'v':
					msg[i] = 22
				elif msg[i] == 'w':
					msg[i] = 23
				elif msg[i] == 'y':
					msg[i] = 24
				elif msg[i] == 'x':
					msg[i] = 25
				elif msg[i] == 'z':
					msg[i] = 26
				elif msg[i] == '!':
					msg[i] = 27
				elif msg[i] == '.':
					msg[i] = 28
				elif msg[i] == ',':
					msg[i] = 29
				elif msg[i] == '?':
					msg[i] = 30
				elif msg[i] == '"':
					msg[i] = 31
				elif msg[i] == ' ':
					msg[i] = 32
				else:
					print "Invalid syntax, try again. " + "\'" + str(msg[i]) + "\'" + "is not defined."
					message()
			numMsg = msg
			linearTran(numMsg)

		#Apply linear translation based on codex
		def linearTran(msg):
			for i in range(len(msg)):
				msg[i] = (msg[i]+(32+(tran)))%32
				if msg[i] == 0:
					msg[i] = 32
			numCode = msg
			codedMsg(numCode)

		#Convert numeric representation to text
		def codedMsg(msg):
			for i in range(len(msg)):
				if msg[i] == 1:
					msg[i] = 'a'
				elif msg[i] == 2:
					msg[i] = 'b'
				elif msg[i] == 3:
					msg[i] = 'c'
				elif msg[i] == 4:
					msg[i] = 'd'
				elif msg[i] == 5:
					msg[i] = 'e'
				elif msg[i] == 6:
					msg[i] = 'f'
				elif msg[i] == 7:
					msg[i] = 'g'
				elif msg[i] == 8:
					msg[i] = 'h'
				elif msg[i] == 9:
					msg[i] = 'i'
				elif msg[i] == 10:
					msg[i] = 'j'
				elif msg[i] == 11:
					msg[i] = 'k'
				elif msg[i] == 12:
					msg[i] = 'l'
				elif msg[i] == 13:
					msg[i] = 'm'
				elif msg[i] == 14:
					msg[i] = 'n'
				elif msg[i] == 15:
					msg[i] = 'o'
				elif msg[i] == 16:
					msg[i] = 'p'
				elif msg[i] == 17:
					msg[i] = 'q'
				elif msg[i] == 18:
					msg[i] = 'r'
				elif msg[i] == 19:
					msg[i] = 's'
				elif msg[i] == 20:
					msg[i] = 't'
				elif msg[i] == 21:
					msg[i] = 'u'
				elif msg[i] == 22:
					msg[i] = 'v'
				elif msg[i] == 23:
					msg[i] = 'w'
				elif msg[i] == 24:
					msg[i] = 'x'
				elif msg[i] == 25:
					msg[i] = 'y'
				elif msg[i] == 26:
					msg[i] = 'z'
				elif msg[i] == 27:
					msg[i] = '!'
				elif msg[i] == 28:
					msg[i] = '.'
				elif msg[i] == 29:
					msg[i] = ','
				elif msg[i] == 30:
					msg[i] = '?'
				elif msg[i] == 31:
					msg[i] = '"'
				elif msg[i] == 32:
					msg[i] = " "
				else:
					print "Invalid syntax. " + "\'" + str(msg[i]) + "\'" + "is not defined."
					message()
			codeMsg = msg
			tmpCode = ""
			for i in range(len(codeMsg)):
				tmpCode = str(tmpCode) + str(codeMsg[i])
			return tmpCode

		tran = LinExt(codex)
		message()
	
	CodeCreate()
	msg = "["+userName+"]" + " " + tmpCode
	msg.replace(';','')
	s.send("t"+msg)

s.close()