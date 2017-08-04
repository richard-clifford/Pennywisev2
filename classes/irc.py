import socket
import ssl

class IRC:

	_sockfd = None
	_connection = None
	# def __init__(self):
	# 	if self._sockfd == None:
	# 		self._sockfd = self.server_connect(self.server, self.port)

	def raw_connect(self, server, port, use_ssl = False):
		self._sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self._sockfd.settimeout(5)

		if use_ssl == True:
			context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
			context.verify_mode = ssl.CERT_REQUIRED
			context.check_hostname = False
			context.load_default_certs()

			# Might need to make this more dynamic - search server for possible versions and ciphers
			wraped_socket = context.wrap_socket(self._sockfd)
			wraped_socket.connect((server, port))
		else:
			wraped_socket = self._sockfd.connect((server, port))

		self._connection = wraped_socket
		return self


	def server_send_data(self, data):
		while True:
			print self._connection.send()

	def set_nick(self, nick):
		pass


ircBot = IRC()
connection = ircBot.raw_connect("irc.darkscience.net", 6697, True)
connection.server_send_data("blah")
