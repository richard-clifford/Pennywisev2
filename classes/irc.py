import socket
import ssl

class IRC:

    _sockfd = None
    _connection = None
    # def __init__(self):
    #   if self._sockfd == None:
    #       self._sockfd = self.server_connect(self.server, self.port)

    def raw_connect(self, server, port, use_ssl = False):
        self._sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self._sockfd.settimeout(0)

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
        data = data + "\r\n"
        sent = self._connection.send(data.encode("UTF-8"))
        return sent

    def server_get_data(self):
        return self._connection.recv(2048).decode("UTF-8")

    def set_nick(self, nick):
        pass

    def say(self, channel, message):
        return self.server_send_data("PRIVMSG %s :%s" % (channel, message))

    def join(self, channel):
        return self.server_send_data("JOIN %s", % (channel))

    def join(self, channel):
        return self.server_send_data("PART %s", % (channel))

    def create_instance(self, server="irc.darkscience.net", port=6697, use_ssl=True, nick="Pennywise", ident="Pennywise"):
        connection = self.raw_connect("irc.darkscience.net", 6697, True)
        connection.server_send_data("USER %s %s %s :%s" % (ident,ident,ident,ident,))
        connection.server_send_data("NICK Pennywise")
        return connection


