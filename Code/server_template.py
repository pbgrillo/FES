import socket

class Server(object):
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.bind(('localhost', 22577)) 
	#port doesn't matter just has to be the same
	
	server.listen()
	while True:
		connection, address = server.accept()
		command = connection.recv(16) #16 bits can be adjusted
		# print(command) # test print of the data sent
		
		if 'Some Action' in str(command):
			#call some function then return back to Lab_View
			connection.sendall('the data from the action')
		elif 'Quit' in str(command):
			break;
	server.close()
