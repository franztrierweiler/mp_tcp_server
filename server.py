#!/usr/bin/python

import socket

# Parameters
HOST = ''
PORT = 1973
NB_MAX_CONNECTIONS = 1
NB_SIZE_BLOCK = 16

def get_data_block(data_socket, size):
	"""Get a block of at most size bytes from the socket data_socket"""
	#Blocking connection
	_data = data_socket.recv(size)
	return _data
	
def get_data(data_socket, eof_value):
	"""Get data until eof value if found at end of received data block"""
	terminate_get = False
	while (terminate_get == False):
		_data = get_data_block(data_socket, NB_SIZE_BLOCK)
		print _data, "->", len(_data)
	return _data

def close_connection(connection):
	connection.close()

def run_incoming_connection(nb_connections, waiting_socket):
	print "Listenning to port: ", PORT
	waiting_socket.listen(nb_connections);

	# Wait for connection on waiting socket
	_conn, _addr = waiting_socket.accept();
	print "Incoming connection detected from: ", _addr

	# Use new socket _conn to exchange data
	_data = get_data(_conn, "A")
	close_connection(_conn)

def launch_server():
	print "Start server"

	# Create waiting socket
	_s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
	_s.bind((HOST, PORT))
	run_incoming_connection(NB_MAX_CONNECTIONS, _s)

if __name__ == "__main__":
	launch_server()