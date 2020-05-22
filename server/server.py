from threading import Thread

import socket
import json

class Server:
	#take sever file as parameter: path for json file
	#serv_file:str
	def __init__(self, serv_file):
		print("Server starting..")

		#constructors
		self.serv_file = serv_file
		self.connected = {}
		self.shut = False
		#take serv_file which contains settings for server
		with open(self.serv_file) as config_file:
			config = json.load(config_file)
			self.host = config["server_settings"]["host"]
			self.port = config["server_settings"]["port"]

		print("Host address	: {}".format(self.host))
		print("Port used	: {}".format(self.port))

		#creating server
		#try:
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.bind((self.host, self.port))
		#except socket.error as soc_ex:
		#	print("Error found. Could'nt create socket. \"{soc_ex}\"")
		#	return
		# set to true when server needs to be closed
		
		


	def new_client_thread(self, client, c_addr):

		#when a new client is connecting to the server
		thr = Thread(target = self.client_thread, args = (client, c_addr))
		thr.start()
		self.connected[client]["client_thread"] = thr

	def client_thread(self, client, c_addr):

		client.send("Server connected".encode())
		connected = True


		while connected:
			try:
				i = 0
				client.send("{}".format(i).encode())
			except Exception as client_ex:
				print("Exception found. \"{}\"".format(client_ex))
				continue
		client.close()


	def start_server(self):

		print("Trying server..")
		try:
			while True:
				connection, ip_addr = self.sock.accept()
				print("Server started. {} connected.".format(ip_addr))
				self.new_client_thread(connection, ip_addr)

		#when the server fails, immediately shut everything
		except KeyboardInterrupt as s_ex:
			print("Server shutting down.")
			self.shut = True
			for c in self.connected:
				c.close()
			print("Disconnected")
			self.sock.close()

	#def main(self):
		
		

if __name__ == '__main__':
	test_server = Server("server_cf.json")
	test_server.start_server()






