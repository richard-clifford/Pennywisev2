from classes.irc import IRC
from classes.config import Config
from classes.plugins import Plugins

import argparse
import json

def main():
    parser = argparse.ArgumentParser(description='Arguments for Pennywise')
    parser.add_argument('-c', '--connection-name', required=True, help='Connection name')
    parser.add_argument('-v', '--verbose', help='Connection name')
    arguments = parser.parse_args()

    verbose = arguments.verbose

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

    plugins = Plugins()
    plugins.load_modules()


    i = 0
    while True:
        data = pennywise.server_get_data()
        if verbose:
            print data

        plugins.process_command(data)

        # Reply with ping
        if data[:4] == 'PING':
            pennywise.send_pong(data)

        # Join Channels
        if i == 10:
            for channel in json.loads(default_channels):
                pennywise.join(channel)

        i = i+1

if __name__ == '__main__':
    main()