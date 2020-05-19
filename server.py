from threading import Thread

import socket
import json

class Server:
	#constructor
	#take sever file as parameter: path for json file
	#serv_file:str
	def __init__(self, serv_file):
		print("Server starting..")

		self.serv_file = serv_file
		self.connected = {}

		#take serv_file which contains settings for server
		with open(self.serv_file) as config_file:
			config = json.load(config_file)
			self.host = config["settings"]["host"]
			self.port = config["settings"]["port"]

		print("Host address	: {self.host")
		print("Port used	: {self.port")

		#creating server
		try:
			self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.sock.bind((self.host, self.port))
		except socket.error as soc_ex:
			print("Error found. Could'nt create socket. \"{soc_ex}\"")
			return

		#needed later
		self.shut = False


	def new_client_thread(self, client, c_addr):

		#when a new client is connecting to the server
		thr = Thread(target = self.client_thread, args = (client, c_addr))
		thr.start()
		self.connected[client]["client_thread"] = thr

	def client_thread(self, client, c_addr):

		client.send("Server connected".encode())
		connected = True


		while connected and not self.shut:
			try:
				i = 0
				client.send({i}.encode())
			except Exception as client_ex:
				print("Exception found. \"{client_ex}\"")
				continue
		client.close()


	def start_server(self):

		print("Trying server..")
		try:
			while True:
				connection, ip_addr = self.sock.accept()
				print("Server started. {ip_addr} connected.")
				self.new_client_thread(connection, ip_addr)

		#when the server fails, immediately shut everything
		except socket.error as s_ex:
			print("Server shutting down.")
			self.shut = True
			for c in self.connected:
				connection.close()
			print("Disconnected")
			self.sock.close()

	#def main(self):
		

if __name__ == '__main__':
	test_server = Server("server_cf.json")
	test_server.start_server()






