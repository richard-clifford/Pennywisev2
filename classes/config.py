import sqlite3
import os

class Config:

    _conn = None
    _connection_name = None

    def __init__(self, connection_name):
        self._connection_name = connection_name
        _conn = self.connect()

    def connect(self):
        database = './databases/%s.db' % (self._connection_name,)
        self._conn = sqlite3.connect(database)
        return self._conn

    def __install(self, connection_name):
        create_config = """CREATE TABLE `config` (
            `name`   TEXT NOT NULL UNIQUE,
            `value`    TEXT NOT NULL UNIQUE,
            `active`   INTEGER NOT NULL,
        );"""

        db = self.connect()
        db.execute(create_config)
        db.commit()
        db.close()

    def get_item(self, config_name):
        db = self.connect()
        query = db.execute("SELECT value FROM config WHERE name=?", (config_name,))
        results = query.fetchone()
        return results
