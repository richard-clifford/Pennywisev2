import os
import json
from classes.config import Config

class Plugins:

    _plugins = []
    _commands = []

    def __init__(self):
        self._plugins = []
        self._commands = []
        return

    def load_modules(self):
        for path, dirs, files in os.walk('modules/'):
            if 'config.json' in files:
                plugin_name = path[8:]
                file = open(path + os.sep + 'config.json', 'r')
                commands = json.loads(file.read())['commands']
                self._commands.append({plugin_name: commands})
                self._plugins.append(plugin_name)
        return self

    def process_command(self, data):
        config = Config('darkscience_new')
        command = data[data.find('PRIVMSG '):].split(':')

        if command[1][1:1] == config.get_item('bot.command_char')[0]:
            print command[1], command[1:1]
            len = data.find(' ')
            if len != -1:
                for plugin in self._plugins:
                    print plugin
                # if data[1:len] in