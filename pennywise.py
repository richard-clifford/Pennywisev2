from classes.irc import IRC
from classes.config import Config

import argparse
import json

def main():
    parser = argparse.ArgumentParser(description='Arguments for Pennywise')
    parser.add_argument('-c', '--connection-name', required=True, help='Connection name')
    arguments = parser.parse_args()
    print arguments.connection_name

    config = Config(arguments.connection_name)

    # Bot Server Configs
    server = config.get_item('server.connection_address')[0]
    port = int(config.get_item('server.connection_port')[0])
    use_ssl = bool(config.get_item('server.connection_use_ssl')[0])

    #Bot specific
    default_channels = config.get_item('bot.default_channels')[0]
    bot_name = config.get_item('bot.nick')[0]
    bot_ident = config.get_item('bot.ident')[0]

    ircBot = IRC()
    pennywise = ircBot.create_instance(server, port, use_ssl, bot_name, bot_ident)

    i = 0

    while True:
        data = pennywise.server_get_data()
        print data

        # Reply with ping
        if data[:4] == 'PING':
            pennywise.server_send_data(("PONG %s" % data.split(' ')[1]))

        # Join Channels
        if i == 10:
            for channel in json.loads(default_channels):
                pennywise.server_send_data(("JOIN %s" % (channel,)))
                pennywise.say("#treehouse", "What's up! :)")

        i = i+1

if __name__ == '__main__':
    main()